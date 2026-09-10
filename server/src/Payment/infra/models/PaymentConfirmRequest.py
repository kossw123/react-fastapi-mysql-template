from pydantic import BaseModel
from uuid import uuid4
from src.Payment.domain.PaymentStatus import PaymentStatus

class PaymentConfirmRequest(BaseModel):
    id: uuid4
    order_id: uuid4
    payment_key: uuid4
    amount: int
    status: PaymentStatus
    confirm_idempotency_key: str
    confirmation_resut: str
    processing_started_at: str
    updated_at: str