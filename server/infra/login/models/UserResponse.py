from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    username: Optional[str] | None