from pydantic import BaseModel
from src.Order.infra.models.OrderItemRequest import OrderItemRequest

class OrderRequest(BaseModel):
    items: list[OrderItemRequest]
