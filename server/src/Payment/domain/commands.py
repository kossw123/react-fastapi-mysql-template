from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler



class CreatePayment(ICommand):       # 결제 생성
    def __init__(self):
        pass

class ConfirmPayment(ICommand):      # 결제 승인
    def __init__(self):
            pass

class CancelPayment(ICommand):       # 결제 취소
    def __init__(self):
            pass

class PartialCancelPayment(ICommand):        # 결제 부분 취소
    def __init__(self):
            pass

class CreatePaymentHandler(ICommandHandler):       # 결제 생성
    def handle(self):
        pass

class ConfirmPaymentHandler(ICommandHandler):      # 결제 승인
    def handle(self):
            pass

class CancelPaymentHandler(ICommandHandler):       # 결제 취소
    def handle(self):
            pass

class PartialCancelPaymentHandler(ICommandHandler):        # 결제 부분 취소
    def handle(self):
            pass







