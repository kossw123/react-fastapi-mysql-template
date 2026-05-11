from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher
from src.shared.Repository import InMemoryStore

def global_bootstrap():
    event_dispatcher = EventDispatcher()
    command_bus = CommandBus()
    product_memoryStore = InMemoryStore()

    return {
        "eventDispatcher": event_dispatcher,
        "commandBus": command_bus,
        "product_memoryRepository": product_memoryStore 
    }



