from src.shared.AggregateRoot import AggregateRoot
from contextlib import contextmanager
from src.Payment.domain.PaymentStatus import PaymentStatus
from uuid import uuid4, UUID
from src.Payment.domain.events import PaymentCreated
from datetime import datetime, timezone

class Payment(): 
    def __init__(
        self,
        id: UUID,
        order_id: UUID,
        amount: int,
        status: PaymentStatus | None,
        payment_key: str | None,
        confirm_idempotency_key: str | None,
        processing_started_at: datetime | None,
        confirmation_result: str | None,
    ):
        self.root = AggregateRoot()
        self.id: UUID = id
        self.order_id = order_id
        self.amount = amount
        self.status = status
        self.payment_key = payment_key
        self.confirm_idempotency_key = confirm_idempotency_key
        self.processing_started_at = processing_started_at
        self.confirmation_result = confirmation_result
        


    @classmethod
    def create(cls, order_id: UUID, amount: int):
        if amount <= 0:
            raise ValueError("결제 금액은 0보다 커야 합니다.")

        payment = cls(
            id=uuid4(),
            order_id=order_id,
            amount=amount,
            status=PaymentStatus.READY,
            payment_key=None,
            confirm_idempotency_key=str(uuid4()),
            processing_started_at=datetime.now(timezone.utc),
            confirmation_result=None,
        )

        payment.root.register(PaymentCreated())

        return payment

    @classmethod
    def restore(
        cls,
        *,
        id: UUID,
        order_id: UUID,
        amount: int,
        status: PaymentStatus,
        payment_key: str | None,
        confirm_idempotency_key: str,
        confirmation_result: dict | None,
        processing_started_at: datetime | None,
    ):
        return cls(
            id=id,
            order_id=order_id,
            amount=amount,
            status=status,
            payment_key=payment_key,
            confirm_idempotency_key=confirm_idempotency_key,
            confirmation_result=confirmation_result,
            processing_started_at=processing_started_at,
        )

    def ready(self):
        if self.status == "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.READY
        self.root.register(PaymentCreated())

    def processing(self):   # 승인 작업을 진행중
        if self.status == "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.PROCESSING
        # self.root.register(CreatedPayment())

        
    def completed(self):    # 승인 성공을 확인하고 DB에도 반영함
        if self.status == "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.COMPLETED
        # self.root.register(CreatedPayment())
    def failed(self):       # 승인 실패가 확정됨
        if self.status == "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.FAILED
        # self.root.register(CreatedPayment())


    def unknown(self):     # 요청은 했지만 승인 결과를 확정하지 못함
        if self.status == "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.UNKNOWN
        # self.root.register(CreatedPayment())


    @contextmanager
    def command_context(self):
        with self.uow:
            yield
        self._publish_events()

    def _publish_events(self):
        while True:
            events = self.uow.collect_events()
            if not events:
                break
            self.dispatcher.dispatch(events)