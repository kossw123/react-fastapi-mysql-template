from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import ConfigDict
from uuid import uuid4, UUID


class ProductModel(SQLModel, table=True):
    id: UUID = Field(
        default = uuid4,
        primary_key=True)
    name: str
    price: int
    status: Optional[str] | None = Field(default=None)

    model_config = ConfigDict(strict=True)
