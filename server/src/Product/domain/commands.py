from typing import TYPE_CHECKING
from src.Product.domain.Product import Product
from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler


if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork


class ProductCreate(ICommand):
    def __init__(self, 
                 id: int, 
                 name: str, 
                 price: int):
        self.id = id
        self.name = name
        self.price = price


class ProductCreateHandler(ICommandHandler):
    def handle(self, 
               command: ProductCreate, 
               uow: UnitOfWork):
        product = Product.create(command.id, command.name, command.price)
        print("[COMMAND: ProductCreateHandler]: product info = ", product.id, "+", product.name)
        uow.product_repository.save(product)
        uow.domain_register(product)
        return product
    

class ProductDiscontinue(ICommand):
    def __init__(self, 
                 id: int):
        self.id = id

class ProductDiscontinueHandler(ICommandHandler):
    def handle(self, 
               command: ProductDiscontinue, 
               uow: UnitOfWork):
        product: Product = uow.product_repository.find(command.id) 
        product.discontinued()
        uow.product_repository.delete(product.id)
        uow.domain_register(product)
        return product
