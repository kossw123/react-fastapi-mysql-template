from src.shared_interface.IEvent import IEvent
from src.shared_interface.IEventHandler import IEventHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork

class OrderCreated(IEvent):
    def __init__(self, 
                 order_id, 
                 customer_id, 
                 items):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items


class OrderCreatedHandler(IEventHandler):
    def handle(self, 
               event: OrderCreated,
               uow: UnitOfWork):
        print(f"[EVENT] OrderCreated | order_id={event.order_id} customer_id={event.customer_id}")
        print("   현재 주문된 내역")
        for item in event.items:
            print(f"      Product_id:{item.product_id} | Quantity:{item.quantity} | total:{item.total()}")