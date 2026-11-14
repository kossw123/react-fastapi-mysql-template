from typing import TYPE_CHECKING
from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler
from src.Payment.domain.Payment import Payment
from dataclasses import dataclass
from uuid import UUID, uuid4
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
@dataclass(frozen=True)
class CreatePayment(ICommand):       # 결제 생성
    id: UUID
    order_id: UUID
    amount: int
    payment_key: str | None



# 원칙적으로 트랜잭션 커밋은 Application Layer가 관리하고 Handler에서는 데이터 변경만 수행하는게 좋다.
# 아래 코드가 왜 필요한지 모르겠다. 이미 하고 있지 않나?
class CreatePaymentHandler(ICommandHandler):
    def handle(self, command: CreatePayment, uow: UnitOfWork):
        logger.info("[CreatePaymentHandler] handle start...")
        repo = uow.payment_respository

        with uow:
            payment = repo.find_by_order_id(
                command.order_id,
                for_update=True
            )
            
            if payment is not None:
                logger.info(
                    f"[CreatePaymentHandler] "
                    f"Existing Payment: {payment.id}"
                )
                return payment
            
            payment = Payment.create(
                order_id=command.order_id,
                amount=command.amount,
            )

            logger.info(
                f"[CreatePaymentHandler] "
                f"New Payment ID: {payment.id}"
            )

            logger.info(
                f"[CreatePaymentHandler] "
                f"New Payment Order ID: {payment.order_id}"
            )

            repo.save(payment)
            uow.domain_register(payment)

        # 6. UoW 종료 시 Commit
        return payment

class ConfirmPayment(ICommand):
    order_id: UUID

class ConfirmPaymentHandler(ICommandHandler):      # 결제 승인
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ConfirmPaymentHandler")
        payment = uow.payment_respository.find_by_order_id(command.order_id, for_update=False)
        with uow:
            uow.payment_respository.save(payment)
            uow.domain_register(payment)

class CancelPaymentHandler(ICommandHandler):       # 결제 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > CancelPaymentHandler")

class PartialCancelPaymentHandler(ICommandHandler):        # 결제 부분 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ParticalCancelPaymentHandler")