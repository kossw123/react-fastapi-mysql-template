from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from uuid import UUID
from src.Payment.domain.PaymentStatus import PaymentStatus
from typing import Any

# # frontend에서 받는 request
# class PaymentConfirmRequest(BaseModel):
#     order_id: UUID = Field(alias="orderId")
#     payment_key: str = Field(
#         alias="paymentKey",
#         min_length=1,
#         max_length=200,
#     )
#     amount: int = Field(gt=0)



# frontend에서 받는 request
class PaymentConfirmRequest(BaseModel):
    order_id: UUID
    payment_key: str = Field(
        min_length=1,
        max_length=200,
    )
    amount: int = Field(
        gt=0,
        le=100_000_000,
        strict=True,
    )

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    @field_validator("payment_key", mode="before")
    @classmethod
    def normalize_payment_key(cls, value:  Any) -> Any:
        if isinstance(value, str):
            value = value.strip()

        return value

    @field_validator("order_id", mode="before")
    @classmethod
    def normalize_payment_key(cls, value:  Any) -> Any:
        if isinstance(value, str):
            value = value.strip()

        return value

    @model_validator(mode="after")
    def validate_payment_request(self):
        if not self.payment_key:
            raise ValueError("반드시 payment_key가 있어야 합니다.")
        
        return self


