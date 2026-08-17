from typing import TYPE_CHECKING

import logging

if TYPE_CHECKING:
    from src.shared_interface.ICommand import ICommand
    from src.shared_interface.ICommandHandler import ICommandHandler
    from src.shared.UnitOfWork import UnitOfWork

logger = logging.getLogger(__name__)



class CommandBus:
    def __init__(self):
        self.handlers: dict[ICommand, ICommandHandler] = {}

    def register(self, command_type: ICommand, handler: ICommandHandler):
        self.handlers[command_type] = handler

    # def dispatch(self, command: ICommand, uow: UnitOfWork = None):
    #     handler = self.handlers[type(command)]
    #     return handler.handle(command, uow)

    def dispatch(self, command: ICommand, uow: UnitOfWork = None):
        logger.info(f"[BACKEND] [CommandBus.py] CommandBus > dispatch: {type(command).__name__} / START")

        handler = self.handlers[type(command)]
        result = handler.handle(command, uow)

        logger.info(f"[BACKEND] [CommandBus.py] CommandBus > dispatch: {type(command).__name__} / DONE")

        return result
