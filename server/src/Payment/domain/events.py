
from src.shared_interface.IEvent import IEvent
from src.shared_interface.IEventHandler import IEventHandler


class PaymentCreated(IEvent):
    def __init__(self):
        pass

class PaymentProcessed(IEvent):
    def __init__(self):
            pass

class PaymentCompleted(IEvent):
    def __init__(self):
            pass

class PaymentFailed(IEvent):
    def __init__(self):
            pass

class PaymentUnknown(IEvent):
      def __init__(self):
            pass


class PaymentCreatedHandler(IEventHandler):
    def __init__(self):
        pass

class PaymentProcessedHandler(IEventHandler):
    def __init__(self):
            pass

class PaymentCompletedHandler(IEventHandler):
    def __init__(self):
            pass

class PaymentFailedHandler(IEventHandler):
    def __init__(self):
            pass

class PaymentUnknownHandler(IEventHandler):
      def __init__(self):
            pass