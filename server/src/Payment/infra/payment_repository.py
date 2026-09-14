from typing import TYPE_CHECKING
from datetime import datetime, timezone
from sqlmodel import select, update
from server.src.Payment.infra.models.PaymentModel import PaymentModel
from uuid import UUID
if TYPE_CHECKING:
    from sqlmodel import Session
    from src.Payment.domain.Payment import Payment


class PaymentRepository():
    def __init__(self, session: Session):
        self.session = session
        self._mapper = _Mapper()
    def save(self, 
             payment: Payment) -> Payment:
        payment_model = self._mapper._to_orm(payment)
        self.session.add(payment_model)
        self.session.flush()
        self.session.refresh(payment_model)
        return payment
    
    def find_by_order_id(self,
                         order_id: UUID,):
         stmt = select(PaymentModel).where(PaymentModel.order_id == order_id)
         return self.session.exec(stmt).first()

    def try_start_confirmation(self, payment_id, payment_key):
         # UPDATE payments
         # SET
         #   status = 'PROCESSING'
         #   payment_key = :payment_key,
         #   processing_started_at = :now
         # WHERE
         #   id = :payment_id
         #   AND status = 'READY'
         #   AND payment_key IS NULL;
         stmt = update(PaymentModel).where(
              PaymentModel.id == payment_id, 
              PaymentModel.status == "READY", 
              PaymentModel.payment_key.is_(None),
              ).values(
                   status="PROCESSING",
                   payment_key=payment_key,
                   processing_started_at=datetime.now(timezone.utc).replace(tzinfo=None)
              ).execution_options(synchronize_session=False)

         result = self.session.exec(stmt)

         return result.rowcount == 1



# id: UUID
# order_id: UUID
# payment_key: str 
# amount: int
# status: str
# confirm_idempotency_key: str
# confirmation_result: dict
# processing_started_at: datetime

class _Mapper():
    def _to_orm(self, payment: Payment) -> PaymentModel:
        return PaymentModel(
            ##
            ##
        )
    def _to_domain(self, orm: PaymentModel) -> Payment:
            return Payment(
                ##
                ##
            )