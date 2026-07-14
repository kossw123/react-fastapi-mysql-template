from typing import TYPE_CHECKING

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
        print(request.paymentKey)
        print(request.orderId)
        print(request.amount)

        return { 
            "status": "OK",
        }