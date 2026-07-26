from src.shared.EventDispatcher import EventDispatcher
from src.shared.CommandBus import CommandBus
from src.Product.domain.commands import (
    ProductCreate, ProductCreateHandler,
    ProductDiscontinue, ProductDiscontinueHandler
)
from src.Product.domain.events import (
    ProductCreated, ProductCreatedHandler,
    ProductDiscontinued, ProductDiscontinuedHandler
)


from src.Order.domain.commands import (
    OrderCreate, OrderCreateHandler
)
from src.Order.domain.events import (
    OrderCreated, OrderCreatedHandler
)


from src.Payment.domain.commands import (
    CreatePayment, CreatePaymentHandler
)
from src.Payment.domain.events import (
    CreatedPayment, CreatedPaymentHandler
)


event_dispatcher = EventDispatcher()
command_bus = CommandBus()


# CommandBus add
## Product
command_bus.register(ProductCreate, ProductCreateHandler())
command_bus.register(ProductDiscontinue, ProductDiscontinueHandler())
## Order
command_bus.register(OrderCreate, OrderCreateHandler())
## Payment
command_bus.register(CreatePayment, CreatePaymentHandler())




# EventDispatcher add
## Product
event_dispatcher.register(ProductCreated, ProductCreatedHandler())
event_dispatcher.register(ProductDiscontinued, ProductDiscontinuedHandler())

## Order
event_dispatcher.register(OrderCreated, OrderCreatedHandler())

## Payment
event_dispatcher.register(CreatedPayment, CreatedPaymentHandler())

container = {
    "EVENT_DISPATCHER": event_dispatcher,
    "COMMAND_BUS": command_bus,
}
