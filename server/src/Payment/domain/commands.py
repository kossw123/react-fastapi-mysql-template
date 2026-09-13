from typing import TYPE_CHECKING
from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler
from src.Payment.domain.Payment import Payment

from uuid import UUID
import logging

if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork


logger = logging.getLogger(__name__)



# id: UUID,
# order_id: UUID,
# payment_key: str,
# amount: int,
# status: str,
# confirm_idempotency_key: str
# confirmation_result: dict
# processing_started_at: datetime
class CreatePayment(ICommand):       # 결제 생성
    def __init__(self,
            id: UUID,
            order_id: UUID,
            amount: int,
            status: str,):
        self.id = id
        self.order_id = order_id
        self.amount = amount
        self.status = status


class CreatePaymentHandler(ICommandHandler):       # 결제 생성
    def handle(self, command: CreatePayment, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > CreatePaymentHandler") 
        payment = Payment.create(command.order_id, command.amount)

        payment_key = None
        confirm_idempotency_key = None
        confirmation_result = None
        processing_started_at = None

        with uow:
            uow.payment_respository.save(payment)
            uow.domain_register(payment)

        return payment


class ConfirmPaymentHandler(ICommandHandler):      # 결제 승인
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ConfirmPaymentHandler")

class CancelPaymentHandler(ICommandHandler):       # 결제 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > CancelPaymentHandler")

class PartialCancelPaymentHandler(ICommandHandler):        # 결제 부분 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ParticalCancelPaymentHandler")







