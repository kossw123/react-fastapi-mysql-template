
from src.Product.domain.commands import (
    ProductCreate,
    ProductActivate,
    ProductDiscontinue,
)
from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher
from src.shared.UnitOfWork import UnitOfWork

from sqlmodel import Session
from src.Product.infra.product_repository import ProductRepository
from src.Product.infra.product_model import ProductModel
from src.Product.domain.commands import ProductCreateHandler



class ProductService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher, uow: UnitOfWork):
        self.extension = _ProductExtension(bus, dispatcher, uow)

    def create_product(self, id, name, price):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductCreate(id, name, price))

    def activate_product(self, id):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductActivate(id))

    def discontinue_product(self, id):
        with self.extension.command_context():
            self.extension.bus.dispatch(ProductDiscontinue(id))

from contextlib import contextmanager


class _ProductExtension:
    def __init__(self, bus, dispatcher, uow):
        self.bus = bus
        self.dispatcher = dispatcher
        self.uow = uow

    @contextmanager
    def command_context(self):
        with self.uow:
            yield
        self._publish_event()

    def _publish_event(self):
        while True:
            events = self.uow.collect_event()
            if not events:
                break
            self.dispatcher.dispatch(events)

from src.Product.domain.commands import (
    Toy_ProductCreate,
    Toy_ProductCreateHandler
) 
from src.Product.infra.product_model import ProductModel
from src.Product.infra.product_repository import ProductRepository
from src.shared.UnitOfWork import UnitOfWork
from src.shared.EventDispatcher import EventDispatcher
from src.shared.CommandBus import Toy_CommandBus
from src.shared.Repository import InMemoryStore
from src.Product.domain.Product import Product

class Temp_ProductService():
    def __init__(self, 
                    bus: Toy_CommandBus,
                    dispatcher: EventDispatcher,
                    memory_store: InMemoryStore
                ):
        self.bus = bus
        self.dispatcher = dispatcher
        self.memory_store = memory_store

    def create_product(self, product_model: ProductModel, uow: UnitOfWork, db_session: ProductRepository):     


        # 이러면 domain이 생성되고 자동으로 AggregateRoot에 등록된다. 
        # 나중에 EventDispatcher에서 dispatch할 때 생기는 pull_events에 영향을 준다.
        
        command = ProductCreate(
            product_model.id,
            product_model.name,
            product_model.price,
        )
        

        # 1. command 등록 확인 



        # # with self._command_context(session, product_model, domain):
        # #     self.memory_store.save(domain)

        # with uow:
        #     self.bus.register(ProductCreate, ProductCreateHandler)
        #     uow.domain_register(domain)
        #     sql_repo = ProductRepository(session)
        #     sql_repo.add_to_session(domain)

        #     self.bus.dispatch(ProductCreate, )


        #     yield


        #     # 이건 event, 그러면 command는?
        #     while True:
        #         events = uow.collect_event()
        #         if not events:
        #             break
        #         self.dispatcher.dispatch(events)

        #     self.memory_store.save(domain)


        # return domain




    # 이 부분 Application layer의 abstract 객체로 빼서 변환하는 것도 생각
    @contextmanager
    def _command_context(self, session: Session, p_model: ProductModel, domain: Product):
        sql_repo = ProductRepository(session)
        with UnitOfWork(session) as uow:
            uow.domain_register(domain)
            sql_repo.add_to_session(p_model)
            yield
            self._publish_event(uow)

    def _publish_event(self, uow: UnitOfWork):
        while True:
            events = uow.collect_event()
            if not events:
                break
            self.dispatcher.dispatch(events)
