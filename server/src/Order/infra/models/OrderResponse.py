from pydantic import BaseModel
from uuid import UUID
from src.Order.infra.models.OrderItemResponse import OrderItemResponse

class OrderResponse(BaseModel):
    order_id: UUID
    customer_id: UUID
    items: list[OrderItemResponse]