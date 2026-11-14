import requests
from typing import TYPE_CHECKING
from contextlib import contextmanager
from src.Payment.infra.models.PreparedConfirmation import PreparedConfirmation
from src.Payment.domain.PaymentStatus import PaymentStatus
from src.Order.domain.commands import OrderCreate
from src.Order.infra.models.OrderResponse import OrderResponse
from src.Order.infra.models.OrderItemResponse import OrderItemResponse
from src.Order.domain.Order import Order
from src.Payment.domain.commands import CreatePayment
from uuid import uuid4
if TYPE_CHECKING:
    from src.shared.EventDispatcher import EventDispatcher
    from src.shared.CommandBus import CommandBus
    from src.shared.UnitOfWork import UnitOfWork


class CheckoutService:
    def __init__(self, 
                 bus: CommandBus, 
                 uow: UnitOfWork, 
                 dispatcher: EventDispatcher):
        self.bus = bus
        self.uow = uow
        self.dispatcher = dispatcher

    def create_order(self, request):

        with self._command_context():
            order = self.bus.dispatch(
                OrderCreate(request),
                self.uow
            )

            self.bus.dispatch(
                CreatePayment(
                    id=uuid4(),
                    order_id=order.order_id,
                    amount=order.calculate_total_price(),
                    payment_key=None
                ),
                self.uow
            )

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

    def _to_OrderResponse(self, 
                          order: Order):
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
            ],
            status=order.status,
            total_price=order.calculate_total_price()
        )