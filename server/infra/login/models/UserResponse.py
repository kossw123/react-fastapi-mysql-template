from pydantic import BaseModel
from typing import Optional
from jose import jwt

class UserResponse(BaseModel):
    username: Optional[str] | None