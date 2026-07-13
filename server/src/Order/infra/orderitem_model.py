from sqlmodel import SQLModel, Field
from pydantic import ConfigDict
from uuid import UUID
from typing import Optional

class OrderItemModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, 
                              primary_key=True)
    order_id: Optional[UUID] = Field(foreign_key="ordermodel.order_id")
    product_id: UUID
    name: str
    price: int
    quantity: int
    model_config = ConfigDict(strict=True)



