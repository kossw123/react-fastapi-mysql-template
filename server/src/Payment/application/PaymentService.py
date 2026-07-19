from typing import TYPE_CHECKING
import requests
import base64
import os

if TYPE_CHECKING:
    from src.shared.EventDispatcher import EventDispatcher
    from src.shared.CommandBus import CommandBus
    from src.shared.UnitOfWork import UnitOfWork
    from src.Payment.infra.PaymentConfirmRequest import PaymentConfirmRequest


class PaymentService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher):
        self.bus = bus
        self.dispatcher = dispatcher
        # self.mapper = _Mapper()

    def confirm(self, 
                request: PaymentConfirmRequest,
                uow: UnitOfWork):
        print("PaymentService.confirm 진입")
        print(request.paymentKey)
        print(request.orderId)
        print(request.amount)


        secret_key = os.getenv("TOSS_SECRET_KEY")
        auth = base64.b64encode(
            f"{secret_key}:".encode()
            ).decode()

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
        
        result = response.json()

        if result["status"] != "DONE":
            raise Exception("결제 승인 실패")

        print(result["status"])     # DONE
        print(result["method"])     # "간편결제"
        print(result["totalAmount"])    # 123
        
        return result