from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler


class CommandBus:
    def __init__(self):
        self.handlers = {}

    def register(self, command_type: ICommand, handler: ICommandHandler):
        self.handlers[command_type] = handler

    def dispatch(self, command: ICommand):
        handler = self.handlers[type(command)]
        return handler.handle(command)


from src.Product.infra.product_repository import ProductRepository
from src.shared.UnitOfWork import UnitOfWork

class Toy_CommandBus():
    def __init__(self):
        self.handlers: dict[ICommand, ICommandHandler] = {}
    def register(self, command_type: ICommand, handler: ICommandHandler):
        self.handlers[command_type] = handler

    def dispatch(self, command: ICommand, uow: UnitOfWork = None):
        handler = self.handlers[type(command)]
        return handler.handle(command, uow)