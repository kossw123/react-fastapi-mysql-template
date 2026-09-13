from src.shared.AggregateRoot import AggregateRoot
from contextlib import contextmanager
from src.Payment.domain.PaymentStatus import PaymentStatus
from uuid import uuid4, UUID
from src.Payment.domain.events import PaymentCreated

class Payment(): 
    def __init__(self):
        self.root = AggregateRoot()
        self.id: UUID = uuid4()
        self.order_id: UUID = uuid4()
        self.amount: int = 0
        self.status: str = PaymentStatus.NONE


    @classmethod
    def create(cls, order_id: UUID, amount: int):
        if amount <= 0:
            raise ValueError("결제 금액은 0보다 커야 합니다.")

        payment = cls(order_id, amount)
        payment.status = PaymentStatus.READY
        payment.root.register(PaymentCreated())
        return payment


    def ready(self):
        if self.status is "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.READY
        self.root.register(PaymentCreated())

    def processing(self):   # 승인 작업을 진행중
        if self.status is "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.PROCESSING
        # self.root.register(CreatedPayment())

        
    def completed(self):    # 승인 성공을 확인하고 DB에도 반영함
        if self.status is "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "FAILED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.COMPLETED
        # self.root.register(CreatedPayment())
    def failed(self):       # 승인 실패가 확정됨
        if self.status is "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "UNKNOWN":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.FAILED
        # self.root.register(CreatedPayment())


    def unknown(self):     # 요청은 했지만 승인 결과를 확정하지 못함
        if self.status is "READY":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "PROCESSING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "COMPLETED":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status is "FAILED":
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