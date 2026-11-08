from typing import TYPE_CHECKING
from datetime import datetime, timezone
from sqlmodel import select, update
from src.Payment.infra.models.PaymentModel import PaymentModel
from uuid import UUID
from src.Payment.domain.Payment import Payment
if TYPE_CHECKING:
    from sqlmodel import Session
    

 
class PaymentRepository():
    def __init__(self, session: Session):
        self.session = session
        self._mapper = _Mapper()
    def save(self, 
             payment: Payment) -> Payment:
        payment_model = self._mapper._to_model(payment)
        self.session.add(payment_model)
        self.session.flush()
        self.session.refresh(payment_model)
        return payment
    
    def find_by_order_id(self,
                         order_id: UUID,
                         *,
                         for_update: bool,) -> Payment | None:
         stmt = select(PaymentModel).where(PaymentModel.order_id == order_id)

         if for_update:
              stmt = stmt.with_for_update()
         stmt = stmt.execution_options(populate_existing=True)

         model = self.session.exec(stmt).first()

         if model is None:
              return None

         return self._mapper._to_domain(model)

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
                   processing_started_at=datetime.now(timezone.utc)
              ).execution_options(synchronize_session=False)

         result = self.session.exec(stmt)

         return result.rowcount == 1

class _Mapper():
    def _to_model(self, payment: Payment) -> PaymentModel:
        return PaymentModel(
            id=payment.id,
            order_id=payment.order_id,
            payment_key=payment.payment_key,
            amount=payment.amount,
            status=payment.status,
            confirm_idempotency_key=(payment.confirm_idempotency_key),
            confirmation_result=payment.confirmation_result,
            processing_started_at=payment.processing_started_at,
        )

    def _to_domain(self, orm: PaymentModel) -> Payment:
            return Payment(
                order_id=orm.order_id,
                amount=orm.amount,
                status=orm.status,
                payment_key=orm.payment_key,
                confirm_idempotency_key=orm.confirm_idempotency_key,
                confirmation_result=orm.confirmation_result,
            )