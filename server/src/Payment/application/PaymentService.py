from typing import TYPE_CHECKING
from fastapi import HTTPException
import requests
import base64
import os
from contextlib import contextmanager

import logging

from src.Payment.infra.TossPaymentClient import TossPaymentClient

from src.Payment.domain.commands import CreatePayment
from uuid import uuid4
if TYPE_CHECKING:
    from src.shared.EventDispatcher import EventDispatcher
    from src.shared.CommandBus import CommandBus
    from src.shared.UnitOfWork import UnitOfWork
    from src.Payment.infra.models.PaymentConfirmRequest import PaymentConfirmRequest


class PaymentService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher, uow: UnitOfWork):
        self.bus = bus
        self.dispatcher = dispatcher
        self.uow = uow
        self.logger = logging.getLogger(__name__)

    def arrange_confirm(self, request: PaymentConfirmRequest):
        secret_key = os.getenv("TOSS_SECRET_KEY")
        auth = base64.b64encode(
            f"{secret_key}:".encode()
            ).decode()


        self.logger = logging.getLogger(__name__)
        self.logger.info("===== LOKI TEST =====")

        self.logger.info(f"[BACKEND] PaymentService.confirm() > auth: {auth}")
        self.logger.info(f"[BACKEND] PaymentService.confirm() > request.payment_key: {request.payment_key}")
        self.logger.info(f"[BACKEND] PaymentService.confirm() > request.order_id: {request.order_id}")
        self.logger.info(f"[BACKEND] PaymentService.confirm() > request.amount: {request.amount}")

        result = self.__log_payment_status(auth, request).json()
        
        self.__log_payment_confirm(result)

        command = CreatePayment(
            id=uuid4(),
            order_id=request.order_id,
            amount=request.amount,
            status=request.status,
            payment_key=request.payment_key,
            )
                    
        with self._command_context():
            payment = self.bus.dispatch(command, self.uow)
                    
        return payment

    def act_confirm(self, request: PaymentConfirmRequest):
        payment = self.uow.payment_respository.find_by_order_id(request.order_id)

        if payment is None:
            raise HTTPException(status_code=404, detail="결제 정보가 없습니다.")
        if payment.amount != request.amount:
            raise HTTPException(status_code=409, detail="결제 금액이 일치하지 않습니다.")
        if payment.payment_key is not None and payment.payment_key != request.payment_key:
            raise HTTPException(status_code=404, detail="기존 결제키와 일치하지 않습니다.")
        if payment.status == "COMPLETED":
            return 200, payment.confirmation_result
        if payment.status in { "PROCESSING", "UNKNOWN" }:
            return 202, {
                "status": payment.status,
                "order_id": str(payment.order_id)
            }

    @contextmanager
    def _command_context(self):
        with self.uow:
            yield
        self._publish_events()

    def _publish_events(self):
        while True:
            events = self.uow.collect_event()
            if not events:
                break
            self.dispatcher.dispatch(events)

    def __log_payment_status(self, 
                             auth: str,
                             request: PaymentConfirmRequest):
        try:
            response = requests.post(
                    "https://api.tosspayments.com/v1/payments/confirm",
                    headers={
                        "Authorization": f"Basic {auth}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "paymentKey": request.paymentKey,
                        "orderId": request.orderId,
                        "amount": request.amount,
                    }
                )
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > status_code: {response.status_code}")
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > response.text: {response.text}")
        
        except requests.exceptions.HTTPError as http_err:
            # 4xx, 5xx 에러 처리 (예: 404 Not Found, 500 Internal Server Error)
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > HTTPError")
            self.logger.info(f"> HTTP 에러 발생 (상태 코드: {response.status_code}): {http_err}")
            
        except requests.exceptions.ConnectionError:
            # 네트워크 연결 실패, DNS 에러 등
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > ConnectionError")
            self.logger.info("> 네트워크 연결에 실패했습니다. 인터넷 연결이나 URL을 확인하세요.")
            
        except requests.exceptions.Timeout:
            # 설정한 timeout 시간 초과
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > Timeout")
            self.logger.info("> 요청 시간이 초과되었습니다.")
            
        except requests.exceptions.RequestException as err:
            # 기타 모든 requests 관련 에러를 처리하는 최상위 예외
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_status() > RequestException")
            self.logger.info(f"> 알 수 없는 에러 발생: {err}")

        return response

    def __log_payment_confirm(self, result):

        if "status" not in result:
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_confirm()")
            raise Exception(
                f"Toss 승인 실패: {result}"
            )

        if result["status"] != "DONE":
            self.logger.info(f"[BACKEND] PaymentService.__log_payment_confirm()")
            raise Exception(
                f"결제 승인 실패: {result}"
            )
