from pydantic import BaseModel
from uuid import UUID

class OrderItemRequest(BaseModel):
    id: UUID
    name: str
    price: int
    quantity: int
