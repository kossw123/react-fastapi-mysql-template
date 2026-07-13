from typing import TYPE_CHECKING
from src.Product.domain.commands import (
    ProductCreate,
    ProductDiscontinue
)
import uuid
from contextlib import contextmanager
from src.Product.domain.Product import Product

if TYPE_CHECKING:
    from src.shared.EventDispatcher import EventDispatcher
    from src.Product.infra.product_model import ProductModel
    from src.shared_interface.ICommand import ICommand
    from src.shared.UnitOfWork import UnitOfWork
    from src.shared.CommandBus import CommandBus
    from uuid import UUID



class ProductService:
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher):
        self.bus = bus
        self.dispatcher = dispatcher
        self.mapper = _Mapper()

    def create_product(self, 
                       product_model: ProductModel, 
                       uow: UnitOfWork) -> Product:
        phase = _Ochestration(self.bus, self.dispatcher, uow)
        product_id = uuid.uuid4()
        command = ProductCreate(
            product_id,
            product_model.name,
            product_model.price,
        )
        phase._execute_command(command)
        
        product = Product.restore(
            product_id, 
            product_model.name, 
            product_model.price, 
            product_model.status
            )
        
        print(type(product))

        return self.mapper._to_response(product) 
        

    def discontinued_product(self, 
                           product_id: UUID, 
                           uow: UnitOfWork):
        phase = _Ochestration(self.bus, self.dispatcher, uow)    
        command = ProductDiscontinue(product_id)
        phase._execute_command(command)

    def update_product(self,
                       product_id: UUID,
                       product_data: ProductModel,
                       uow: UnitOfWork) -> Product:
        repo = uow.product_repository
        product =  repo.update(product_id, product_data)

        return self.mapper._to_response(product)


class _Ochestration():
    def __init__(self, bus: CommandBus, dispatcher: EventDispatcher, uow: UnitOfWork):
        self.bus = bus
        self.uow = uow
        self.dispatcher = dispatcher

    def _execute_command(self, command: ICommand):
        with self._connect_command(self.uow):
            output = self.bus.dispatch(command, self.uow)

    @contextmanager
    def _connect_command(self, uow: UnitOfWork):
        with uow:
            yield
        self._publish_event(uow)

    def _publish_event(self, uow: UnitOfWork):
        while True:
            events = uow.collect_event()
            if not events:
                break
            self.dispatcher.dispatch(events)
        


class _Mapper():
    def _to_response(self, data: Product):
        return {
            "id": data.id,
            "name": data.name,
            "price": data.price,
            "status": data.status,
        }