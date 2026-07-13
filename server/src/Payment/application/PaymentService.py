from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.shared.EventDispatcher import EventDispatcher
    from src.shared.CommandBus import CommandBus


class PaymentService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher):
        self.bus = bus
        self.dispatcher = dispatcher
        # self.mapper = _Mapper()






