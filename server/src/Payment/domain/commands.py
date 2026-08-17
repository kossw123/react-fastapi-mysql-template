from typing import TYPE_CHECKING
from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler

import logging

if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork


logger = logging.getLogger(__name__)

class CreatePayment(ICommand):       # 결제 생성
    def __init__(self):
        pass

class ConfirmPayment(ICommand):      # 결제 승인
    def __init__(self):
            pass

class CancelPayment(ICommand):       # 결제 취소
    def __init__(self):
            pass

class PartialCancelPayment(ICommand):        # 결제 부분 취소
    def __init__(self):
            pass

class CreatePaymentHandler(ICommandHandler):       # 결제 생성
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > CreatePaymentHandler")

class ConfirmPaymentHandler(ICommandHandler):      # 결제 승인
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ConfirmPaymentHandler")

class CancelPaymentHandler(ICommandHandler):       # 결제 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > CancelPaymentHandler")

class PartialCancelPaymentHandler(ICommandHandler):        # 결제 부분 취소
    def handle(self, command: ICommand, uow: UnitOfWork):
        logger.info(f"[BACKEND] [commands.py] COMMANDHANDLER > ParticalCancelPaymentHandler")







