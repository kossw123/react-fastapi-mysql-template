from abc import abstractmethod
from src.shared_interface.ICommand import ICommand
from src.shared.UnitOfWork import UnitOfWork

class ICommandHandler:
    @abstractmethod
    def handle(self, command: ICommand, uow: UnitOfWork):
        pass
