from pydantic import BaseModel
from uuid import UUID    
from src.Order.infra.models.OrderItemRequest import OrderItemRequest

class OrderRequest(BaseModel):
    items: list[OrderItemRequest]
