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
        print(f"[BACKEND] PaymentService.confirm.TOSS_SECRET_KEY: {secret_key}")
        print(f"[BACKEND] PaymentService.confirm.TOSS_SECRET_KEY Type: {type(secret_key)}")    
        auth = base64.b64encode(
            f"{secret_key}:".encode()
            ).decode()

        print(f"[BACKEND] PaymentService.confirm.auth: {auth}")


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

        print(f"[BACKEND] PaymentService.confirm status_code: {response.status_code}")
        print(f"[BACKEND] PaymentService.confirm response.text: {response.text}")

        result = response.json()
        self.__logging(result)

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


    def __logging(self, result):

        if "status" not in result:
            raise Exception(
                f"Toss 승인 실패: {result}"
            )

        if result["status"] != "DONE":
            raise Exception(
                f"결제 승인 실패: {result}"
            )