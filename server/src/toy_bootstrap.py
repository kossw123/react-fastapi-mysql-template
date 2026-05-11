from src.shared.EventDispatcher import EventDispatcher
from src.shared.CommandBus import CommandBus
from src.shared.Repository import InMemoryStore
from src.Product.domain.commands import *
from src.Product.infra.product_repository import ProductRepository


class global_config():
    def global_bootstrap(self):
        self.event_dispatcher = EventDispatcher()
        self.command_bus = CommandBus()
        self.product_memoryStore = InMemoryStore()
        

        return {
            "EVENT_DISPATCHER": self.event_dispatcher,
            "COMMAND_BUS": self.command_bus,
            "PRODUCT_MEMORY_REPOSITORY": self.product_memoryStore,
        }
    def product_create_command(self):
        self.command_bus.register(ProductCreate, Toy_ProductCreateHandler(self.product_memoryStore))
        print("command 등록 완료")
