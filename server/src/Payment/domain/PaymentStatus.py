from enum import Enum

class PaymentStatus(Enum):
    NONE = "NONE"
    PENDING = "PENDING"     
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIALLY_CANCELED = "PARTIALLY_CANCELED"
    CANCELED = "CANCELED"