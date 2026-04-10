from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher
from src.shared.UnitOfWork import UnitOfWork
from src.Product.domain.commands import (
    ProductCreate,
    ProductActivate,
    ProductDiscontinue,
)


class ProductService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher, uow: UnitOfWork):
        self.extension = __ProductExtension(bus, dispatcher, uow)

    def create_product(self, id, name, price):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductCreate(id, name, price))

    def activate_product(self, id):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductActivate(id))

    def discontinue_product(self, id):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductDiscontinue(id))


class __ProductExtension:
    def __init__(self, bus, dispatcher, uow):
        self.bus = bus
        self.dispatcher = dispatcher
        self.uow = uow

    def command_context(self):
        with self.uow:
            yield
        self._publish_events()

    def _publish_event(self):
        while True:
            events = self.uow.collect_events()
            if not events:
                break
            self.dispatcher.dispatch(events)
