from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from sqlmodel import Session
    from src.Payment.domain.Payment import Payment


class PaymentRepository():
    def __init__(self, session: Session):
        self.session = session
    def save(self, 
             payment: Payment) -> Payment:
        self.session.add(payment_model)
        self.session.flush()
        self.session.refresh(payment_model)
        return payment