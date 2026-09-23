from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True)
class PreparedConfirmation:
    payment_id: UUID
    acquired: bool

    toss_argument: dict | None = None
    response_status: int | None = None
    response_body: dict | None = None