from src.Order.domain.commands import (
    OrderCreate
)
from src.Order.infra.models.OrderResponse import OrderResponse
from contextlib import contextmanager
from typing import TYPE_CHECKING
from src.Order.infra.models.OrderItemResponse import OrderItemResponse

if TYPE_CHECKING:
    from src.shared.CommandBus import CommandBus
    from src.shared.EventDispatcher import EventDispatcher
    from src.shared.UnitOfWork import UnitOfWork
    from src.Order.infra.models.OrderRequest import OrderRequest


class OrderService:
    def __init__(self, 
                 command_bus: CommandBus, 
                 dispatcher: EventDispatcher, 
                 uow: UnitOfWork):
        self.bus = command_bus
        self.dispatcher = dispatcher
        self.uow = uow

    def create_order(self, 
                    request: OrderRequest):
        command = OrderCreate(request)

        with self._command_context():
            order = self.bus.dispatch(command, self.uow)
        return self._to_OrderResponse(order)


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


    def _to_OrderResponse(self, order):
        return OrderResponse(
            order_id=order.order_id,
            customer_id=order.customer_id,
            items=[
                OrderItemResponse(
                    id=item.product_id,
                    name=item.name,
                    price=item.price,
                    quantity=item.quantity,
                )
                for item in order.items
            ]
        )