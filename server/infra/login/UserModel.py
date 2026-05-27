from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import ConfigDict
from uuid import uuid4, UUID

class UserModel(SQLModel, table=True):
    id: UUID = Field(
        default = uuid4,
        primary_key=True)
    name: str
    password: str

    model_config = ConfigDict(strict=True)