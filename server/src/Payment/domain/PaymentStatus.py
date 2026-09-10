from enum import Enum

class PaymentStatus(Enum):
    NONE = "NONE"
    PENDING = "PENDING"     
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIALLY_CANCELED = "PARTIALLY_CANCELED"
    CANCELED = "CANCELED"




# Payment Idempotency Key를 위한 Status
class _untitle(Enum):
    READY = 0
    PROCESSING = 1
    COMPLETED = 2
    FAILED = 3
    UNKNOWN = 4