from pydantic import BaseModel
from uuid import UUID

class OrderItemResponse(BaseModel):
    id: UUID
    name: str
    price: int
    quantity: int
