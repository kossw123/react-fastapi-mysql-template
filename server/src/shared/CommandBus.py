from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.shared_interface.ICommand import ICommand
    from src.shared_interface.ICommandHandler import ICommandHandler
    from src.shared.UnitOfWork import UnitOfWork


class CommandBus:
    def __init__(self):
        self.handlers: dict[ICommand, ICommandHandler] = {}

    def register(self, command_type: ICommand, handler: ICommandHandler):
        self.handlers[command_type] = handler

    # def dispatch(self, command: ICommand, uow: UnitOfWork = None):
    #     handler = self.handlers[type(command)]
    #     return handler.handle(command, uow)

    def dispatch(self, command: ICommand, uow: UnitOfWork = None):
        print(f"[COMMAND] {type(command).__name__}")

        handler = self.handlers[type(command)]
        result = handler.handle(command, uow)

        print(f"[COMMAND DONE] {type(command).__name__}")

        return result
