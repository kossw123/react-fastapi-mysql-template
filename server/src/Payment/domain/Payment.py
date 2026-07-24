from src.shared.AggregateRoot import AggregateRoot
from contextlib import contextmanager
from src.Payment.domain.PaymentStatus import PaymentStatus
from uuid import uuid4

class Payment(): 
    def __init__(self):
        self.root = AggregateRoot()
        self.id = uuid4()
        self.order_id : str = None
        self.customer_id : str = None
        self.amount : int = 0
        self.status = PaymentStatus.NONE


    # PENDING = "PENDING"                           보류
    # COMPLETED = "COMPLETED"                       결제 완료
    # FAILED = "FAILED"                             결제 실패
    # PARTIALLY_CANCELED = "PARTIALLY_CANCELED"     결제 부분 취소
    # CANCELED = "CANCELED"                         결제 취소



    def pending(self):      # 보류
        if self.status == "PENDING":
            raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "COMPLETED":
                    raise Exception(f"Not Confirm Payment, Current status is {self.status}")
        if self.status == "FAILED":
                    raise Exception(f"Not Confirm Payment, Current status is {self.status}")

        self.status = PaymentStatus.PENDING

        

        self.root.register()

    def completed(self):        # 결제 완료
        pass
    def failed(self):       # 결제 시도 실패
        pass
    def partially_canceled(self):   # 결제 부분 취소
        pass
    def canceled(self):     # 결제 취소
        pass

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