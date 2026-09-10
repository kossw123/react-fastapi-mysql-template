from typing import TYPE_CHECKING

from sqlmodel import select
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


    def create(self, 
               order_id: UUID,
               amount: int):
        
        payment = PaymentModel(
            order_id = order_id,
            amount = amount
        )

        self.session.add(payment)
        self.session.flush()
        self.session.refresh(payment)
        return payment


    def find_by_order_id(self,
                         order_id: UUID,):
         stmt = select(PaymentModel).where(PaymentModel.order_id == order_id)
         return self.session.exec(stmt).first()




class _Mapper():
    def _to_orm(self, product: Payment) -> PaymentModel:
        return PaymentModel(
            ##
            ##
        )
    def _to_domain(self, orm: PaymentModel) -> Payment:
            return PaymentModel(
                ##
                ##
            )