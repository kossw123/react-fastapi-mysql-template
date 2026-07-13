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


from src.Order.domain.commands import (
    OrderCreate, OrderCreateHandler
)
from src.Order.domain.events import (
    OrderCreated, OrderCreatedHandler
)


event_dispatcher = EventDispatcher()
command_bus = CommandBus()


# CommandBus add
## Product
command_bus.register(ProductCreate, ProductCreateHandler())
command_bus.register(ProductDiscontinue, ProductDiscontinueHandler())
## Order
command_bus.register(OrderCreate, OrderCreateHandler())



# EventDispatcher add
## Product
event_dispatcher.register(ProductCreated, ProductCreatedHandler())
event_dispatcher.register(ProductDiscontinuedHandler, ProductDiscontinuedHandler())

## Order
event_dispatcher.register(OrderCreated, OrderCreatedHandler())


container = {
    "EVENT_DISPATCHER": event_dispatcher,
    "COMMAND_BUS": command_bus,
}
