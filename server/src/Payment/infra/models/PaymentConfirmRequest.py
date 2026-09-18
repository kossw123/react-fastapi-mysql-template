from pydantic import BaseModel, Field
from uuid import UUID
from src.Payment.domain.PaymentStatus import PaymentStatus


# frontend에서 받는 request
class PaymentConfirmRequest(BaseModel):
    order_id: UUID = Field(alias="orderId")
    payment_key: str = Field(
        alias="paymentKey",
        min_length=1,
        max_length=200,
    )
    amount: int = Field(gt=0)
    status: PaymentStatus