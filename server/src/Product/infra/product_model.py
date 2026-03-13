from sqlmodel import SQLModel, Field
from typing import Optional

class ProductModel(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    name: str
    price: int
    status: str