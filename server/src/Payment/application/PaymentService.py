import requests
from typing import TYPE_CHECKING
from fastapi import HTTPException
from contextlib import contextmanager
from src.Payment.infra.models.PreparedConfirmation import PreparedConfirmation
from src.Payment.domain.PaymentStatus import PaymentStatus

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
    def __init__(
            self, 
            bus: CommandBus, 
            dispatcher: EventDispatcher, 
            uow: UnitOfWork,
            toss_client: TossPaymentClient,
            ):
        self.bus = bus
        self.dispatcher = dispatcher
        self.uow = uow
        self.toss_client = toss_client
        self.logger = logging.getLogger(__name__)

    def confirm(self, request: PaymentConfirmRequest):
        return self.act_confirm(request)


        

    def act_confirm(self, request: PaymentConfirmRequest):
            # 반드시 먼저 수행할 것:
            # - 주문 소유자와 결제 가능 상태 검증
            # - payment 존재 여부 확인
            # - amount와 payment_key 일치 여부 확인
            # - COMPLETED면 기존 결과 반환
            # - PROCESSING / UNKNOWN이면 처리 중 응답
            # - READY 이외의 상태는 승인 시작 금지
        repo = self.uow.payment_respository

        with self.uow:
            self.logger.info("[CONFIRM] Payment searching start...")    
            payment = repo.find_by_order_id(request.order_id, for_update=True)
            self.logger.info(f"[CONFIRM] Payment Searching result : {payment}")
            self.logger.info(f"[CONFIRM] Payment status : {payment.status if payment else None}")
            self.logger.info(f"[CONFIRM] Confirm Start...")
            if request.order_id == None:
                raise ValueError("order_id가 없습니다.")
            if payment is None:
                raise HTTPException(status_code=404, detail="결제 정보가 없습니다.")
            if payment.status == PaymentStatus.COMPLETED:
                return 200, payment.confirmation_result
            if payment.status in { PaymentStatus.PROCESSING, PaymentStatus.UNKNOWN }:
                return 202, {
                    "status": payment.status,
                    "order_id": str(payment.order_id)
                }
            if payment.status != PaymentStatus.READY:
                raise ValueError("결제 준비 상태가 아닙니다.")
            if payment.amount != request.amount:
                raise HTTPException(status_code=409, detail="결제 금액이 일치하지 않습니다.")
            if payment.payment_key != None and payment.payment_key != request.payment_key:
                raise HTTPException(status_code=404, detail="기존 결제키와 일치하지 않습니다.")


            # region --- outer API calling

            payment_id = payment.id
            toss_arguments = { 
                "payment_key": request.payment_key,
                "order_id": str(payment.order_id),
                "amount": payment.amount,
                "idempotency_key": payment.confirm_idempotency_key,
            }

            acquired = repo.try_start_confirmation(
                payment_id=payment_id,
                payment_key=request.payment_key
            )

            if acquired:
                result = self.toss_client.confirm(**toss_arguments)
                if result is None:
                    raise ValueError("토스에서 반환받은 승인 결과물이 없습니다.")
                payment.status = PaymentStatus.COMPLETED
                payment.confirmation_result = result

                self.logger.info(f"[CONFIRM] Toss Confirm result : {result}")

        # endregion --- outer API calling
        return payment


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


    def prepare_confirmation(self, request: PaymentConfirmRequest):
        repo = self.uow.payment_respository
        payment = repo.find_by_order_id(request.order_id)

        if payment is None:
            raise HTTPException(
                status_code=404,
                detail="결제 준비 기록이 없습니다.",
            )

        self._validate_confirmation_request(payment, request)

        existing = self._existing_confirmation_result(payment)

        if existing is not None:
            return existing

        if payment.payment_key is not None:
            raise HTTPException(
                status_code=409,
                detail="결제 상태 확인이 필요합니다."
            )

        if not payment.confirm_idempotency_key:
            raise RuntimeError("저장된 승인 멱등키가 없습니다.")

        payment_id = payment.id

        toss_arguments = {
            "payment_key": request.payment_key,
            "order_id": str(payment.order_id),
            "amount": payment.amount,
            "idempotency_key": payment.confirm_idempotency_key,
        }

        acquired = repo.try_start_confirmation(payment_id, request.payment_key)

        if acquired:
            return PreparedConfirmation(
                payment_id=payment_id,
                acquired=True,
                toss_arguments=toss_arguments
            )

        current = repo.find_by_order_id(
            request.order_id,
            for_update=True
        )

        if current is None:
            raise HTTPException(
                status_code=404,
                detail="결제 기록이 없습니다."
            )

        self._validate_confirmation_request(current, request)

        existing = self._exsiting_confirmation_result(current)

        if existing is not None:
            return existing

        raise HTTPException(
            status_code=409,
            detail="결제 상태 확인이 필요합니다."
        )


    def _validate_confirmation_request(self, payment, request):
        if payment.amount != request.amount:
            raise HTTPException(
                status_code=409,
                detail="결제 금액이 일치하지 않습니다.",
            )

        if (
            payment.payment_key is not None
            and payment.payment_key != request.payment_key
        ):
            raise HTTPException(
                status_code=409,
                detail="기존 결제키와 일치하지 않습니다.",
            )

    def _existing_confirmation_result(self, payment):
        if payment.status == PaymentStatus.COMPLETED:
            if payment.confirmation_result is None:
                raise RuntimeError(
                    "완료된 결제의 승인 결과가 없습니다."
                )

            return PreparedConfirmation(
                payment_id=payment.id,
                acquired=False,
                response_status=200,
                response_body=dict(payment.confirmation_result),
            )

        if payment.status in {"PROCESSING", "UNKNOWN"}:
            return PreparedConfirmation(
                payment_id=payment.id,
                acquired=False,
                response_status=202,
                response_body={
                    "status": payment.status,
                    "orderId": str(payment.order_id),
                },
            )

        if payment.status == PaymentStatus.READY:
            return None

        # FAILED 등은 이 경로에서 새 승인으로 재시작하지 않음
        raise HTTPException(
            status_code=409,
            detail="승인을 시작할 수 없는 결제 상태입니다.",
        )