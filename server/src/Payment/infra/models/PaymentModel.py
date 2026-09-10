from datetime import datetime

from sqlmodel import JSON, Column, SQLModel, Field
from pydantic import ConfigDict
from uuid import uuid4, UUID


class PaymentModel(SQLModel, table=True):
    id: UUID = Field(
        default_factory= uuid4,
        primary_key=True
    )
    order_id: UUID = Field(
            default_factory= uuid4,
            primary_key=True
    )


    payment_key: str | None = Field(
        default=None,
        max_length=200,
        unique=True,
    )

    amount: int
    status: str = Field(
        default="READY"
    )

    confirm_idempotency_key: str = Field(
        default_factory=lambda: str(uuid4()),
        max_length=36,
        unique=True,
    )

    confirmation_result: dict | None = Field(
        default=None,
        sa_column=Column(JSON),
    )

    processing_started_at: datetime | None = None

    model_config = ConfigDict(strict=True)
