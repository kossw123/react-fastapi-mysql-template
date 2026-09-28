from abc import abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.shared_interface.IEvent import IEvent
    from src.shared.UnitOfWork import UnitOfWork

class IEventHandler:
    @abstractmethod
    def handle(self, event: IEvent, uow: UnitOfWork):
        pass
