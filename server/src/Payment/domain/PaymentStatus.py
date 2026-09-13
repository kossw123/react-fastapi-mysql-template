from enum import Enum

# Payment Idempotency Key를 위한 Status
class PaymentStatus(Enum):
    NONE = "NONE"   # default
    READY = "READY"   # 아직 승인 처리를 시작하지 않음
    PROCESSING = "PROCESSING"  # 승인 작업을 진행중
    COMPLETED = "COMPLETED"   # 승인 성공을 확인하고 DB에도 반영함
    FAILED = "FAILED"  # 승인 실패가 확정됨
    UNKNOWN = "UNKNOWN" # 요청은 했지만 승인 결과를 확정하지 못함