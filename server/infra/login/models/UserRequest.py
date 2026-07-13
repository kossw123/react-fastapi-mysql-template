from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    username: Optional[str] | None

