from http import HTTPStatus

from fastapi import HTTPException

from src.Order.domain.Order import Order
from src.Order.domain.OrderItem import OrderItem
from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler
from uuid import UUID, uuid4
from src.Order.infra.models.OrderRequest import OrderRequest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork

class OrderCreate(ICommand):
    def __init__(self, 
                 request: OrderRequest):
        self.request = request


class OrderCreateHandler(ICommandHandler):
    def handle(self, 
               command: OrderCreate,
               uow: UnitOfWork):
        order_items = []
        order_id = uuid4()
        customer_id = uuid4()

        if len(command.request.items) == 0:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="empty items"
            )


        for item in command.request.items: 
            order_items.append(
                OrderItem.create(
                    order_id = order_id,
                    name = item.name,
                    product_id = item.id,
                    price = item.price, 
                    quantity = item.quantity
                )
            )

        # def create(cls, id, customer_id, items):
        order = Order.create(order_id=order_id,
                             customer_id=customer_id,
                             items=order_items)
        with uow:
            uow.order_repository.save(order)
            uow.domain_register(order)

        return order