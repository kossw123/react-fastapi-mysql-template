from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher


def global_bootstrap():
    event_dispatcher = EventDispatcher()
    command_bus = CommandBus()

    return {
        "eventDispatcher": event_dispatcher,
        "commandBus": command_bus,
    }
