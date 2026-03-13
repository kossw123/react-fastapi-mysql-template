from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler


class CommandBus():
    def __init__(self):
        self.handlers = {}
    def register(self, command_type: ICommand, handler: ICommandHandler):
        self.handlers[command_type] = handler
    def dispatch(self, command: ICommand):
        handler = self.handlers[type(command)]
        handler.handle(command)