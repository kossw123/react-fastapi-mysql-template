from typing import TYPE_CHECKING
from src.Order.domain.Order import Order
if TYPE_CHECKING:
    from sqlmodel import Session

from src.Order.infra.orderitem_model import OrderItemModel 



# 주문 내역 이력 조회


class OrderRepository():
    def __init__(self, session: Session):
        self.session = session
        self.mapper = _Mapper()
    def save(self, 
             order: Order) -> Order:
        
        order_model = OrderModel(
            order_id = order.order_id,
            customer_id = order.customer_id
        )
        self.session.add(order_model)
    
        for item in order.items:
            self.session.add(OrderItemModel(
                order_id=item.order_id,
                product_id=item.product_id,
                name=item.name,
                price=item.price,
                quantity=item.quantity
            ))
        self.session.flush()
        self.session.refresh(order_model)
        return order
    


from src.Order.infra.order_model import OrderModel

class _Mapper():
    def _to_orm(self, 
                order: Order) -> OrderModel:
        return OrderModel(
            id = order.id,
            customer_id = order.customer_id,
            items = order.products
        )