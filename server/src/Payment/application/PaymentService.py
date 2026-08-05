from typing import TYPE_CHECKING
import requests
import base64
import os
from contextlib import contextmanager

from src.Payment.domain.commands import CreatePayment

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
        # self.mapper = _Mapper()

    def confirm(self, request: PaymentConfirmRequest):
        print(request.paymentKey)
        print(request.orderId)
        print(request.amount)


        secret_key = os.getenv("TOSS_SECRET_KEY")
        auth = base64.b64encode(
            f"{secret_key}:".encode()
            ).decode()

        print(f"[BACKEND] PaymentService.confirm.auth: {auth}")

        result = self.__log_payment_status(auth, request).json()
        
        self.__log_payment_confirm(result)

        command = CreatePayment()
                    
        with self._command_context():
            payment = self.bus.dispatch(command, self.uow)
                    
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
                             request: PaymentConfirmRequest,
                             response: requests):
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
            print(f"[BACKEND] PaymentService.confirm > status_code: {response.status_code}")
            print(f"[BACKEND] PaymentService.confirm > response.text: {response.text}")
        
        except requests.exceptions.HTTPError as http_err:
            # 4xx, 5xx 에러 처리 (예: 404 Not Found, 500 Internal Server Error)
            print(f"[BACKEND] PaymentService.confirm > HTTPError")
            print(f"> HTTP 에러 발생 (상태 코드: {response.status_code}): {http_err}")
            
        except requests.exceptions.ConnectionError:
            # 네트워크 연결 실패, DNS 에러 등
            print(f"[BACKEND] PaymentService.confirm > ConnectionError")
            print("> 네트워크 연결에 실패했습니다. 인터넷 연결이나 URL을 확인하세요.")
            
        except requests.exceptions.Timeout:
            # 설정한 timeout 시간 초과
            print(f"[BACKEND] PaymentService.confirm > Timeout")
            print("> 요청 시간이 초과되었습니다.")
            
        except requests.exceptions.RequestException as err:
            # 기타 모든 requests 관련 에러를 처리하는 최상위 예외
            print(f"[BACKEND] PaymentService.confirm > RequestException")
            print(f"> 알 수 없는 에러 발생: {err}")

        return response

    def __log_payment_confirm(self, result):

        if "status" not in result:
            raise Exception(
                f"Toss 승인 실패: {result}"
            )

        if result["status"] != "DONE":
            raise Exception(
                f"결제 승인 실패: {result}"
            )
