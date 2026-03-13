from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher
from src.shared.UnitOfWork import UnitOfWork
from src.shared.Session import Session

def bootstrap():
    event_dispatcher = EventDispatcher()
    command_bus = CommandBus()
    session = Session()
    uow = UnitOfWork(session)


    return {
        "eventDispatcher": event_dispatcher,
        "commandBus": command_bus,
        "unitOfWork": uow
    }