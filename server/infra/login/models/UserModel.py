from sqlmodel import SQLModel, Field
from pydantic import ConfigDict
from uuid import uuid4, UUID

class UserModel(SQLModel, table=True):
    id: UUID = Field( 
        default_factory = uuid4,
        primary_key=True)
    username: str
    email: str 
    password: str

    model_config = ConfigDict(strict=True) 