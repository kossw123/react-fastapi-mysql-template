from sqlmodel import SQLModel, Field
from pydantic import ConfigDict
from uuid import UUID

class OrderModel(SQLModel, table=True):
    id: int = Field(default=None,
                    primary_key=True)
    order_id: UUID = Field(unique=True)
    customer_id: UUID
    model_config = ConfigDict(strict=True)  