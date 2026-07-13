from src.shared.AggregateRoot import AggregateRoot
from contextlib import contextmanager

class Payment(): 
    def __init__(self):
        self.root = AggregateRoot()
    def authorize(self, id):
        with self.command_context():
            self.command_bus.dispatch(PaymentAuthorize(id))
    def capture(self, order_id, customer_id, payment_id):
        with self.command_context():
            self.command_bus.dispatch(PaymentCapture(order_id, customer_id, payment_id))
    def fail(self, id, customer_id, amount):
        with self.command_context():
            self.command_bus.dispatch(PaymentFail(id, customer_id, amount))
    def refund(self, id, customer_id, amount):
        with self.command_context():
            self.command_bus.dispatch(PaymentRefund(id, customer_id, amount))

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