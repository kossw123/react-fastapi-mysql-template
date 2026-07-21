
from src.shared_interface.IEvent import IEvent
from src.shared_interface.IEventHandler import IEventHandler


class CreatedPayment():       # 결제 생성
    pass

class ConfirmedPayment():      # 결제 승인
    pass

class CanceledPayment():       # 결제 취소
    pass

class PartialCanceledPayment():        # 결제 부분 취소
    pass

class CreatedPaymentHandler():       # 결제 생성
    pass

class ConfirmedPaymentHandler():      # 결제 승인
    pass

class CanceledPaymentHandler():       # 결제 취소
    pass

class PartialCanceledPaymentHandler():        # 결제 부분 취소
    pass

