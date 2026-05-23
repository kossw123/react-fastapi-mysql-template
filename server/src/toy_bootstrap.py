from src.shared.EventDispatcher import EventDispatcher
from src.shared.CommandBus import CommandBus

from src.Product.domain.commands import (
    ProductCreate, ProductCreateHandler,
    ProductDiscontinue, ProductDiscontinueHandler
)
from src.Product.domain.events import (
    ProductCreated, ProductCreatedHandler,
    ProductDiscontinuedHandler
)

event_dispatcher = EventDispatcher()
command_bus = CommandBus()


# CommandBus add
command_bus.register(ProductCreate, ProductCreateHandler())
command_bus.register(ProductDiscontinue, ProductDiscontinueHandler())

# EventDispatcher add
event_dispatcher.register(ProductCreated, ProductCreatedHandler())
event_dispatcher.register(ProductDiscontinuedHandler, ProductDiscontinuedHandler())

container = {
    "EVENT_DISPATCHER": event_dispatcher,
    "COMMAND_BUS": command_bus,
}
