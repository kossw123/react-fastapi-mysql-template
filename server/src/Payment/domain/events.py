
from src.shared_interface.IEvent import IEvent
from src.shared_interface.IEventHandler import IEventHandler


class CreatedPayment(IEvent):       # 결제 생성
    def __init__(self):
        pass

class ConfirmedPayment(IEvent):      # 결제 승인
    def __init__(self):
            pass

class CanceledPayment(IEvent):       # 결제 취소
    def __init__(self):
            pass

class PartialCanceledPayment(IEvent):        # 결제 부분 취소
    def __init__(self):
            pass

class CreatedPaymentHandler(IEventHandler):       # 결제 생성
    def handle(self):
        pass

class ConfirmedPaymentHandler(IEventHandler):      # 결제 승인
    def handle(self):
            pass

class CanceledPaymentHandler(IEventHandler):       # 결제 취소
    def handle(self):
            pass

class PartialCanceledPaymentHandler(IEventHandler):        # 결제 부분 취소
    def handle(self):
            pass

