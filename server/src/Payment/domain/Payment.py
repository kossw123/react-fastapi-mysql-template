from src.shared.AggregateRoot import AggregateRoot
from contextlib import contextmanager

class Payment(): 
    def __init__(self):
        self.root = AggregateRoot()
        self.id
        self.order_id
        self.customer_id
        self.amount
        self.status



    def pending(self):      # 보류
        pass
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