from src.shared_interface.ICommand import ICommand
from src.shared_interface.ICommandHandler import ICommandHandler
from src.Product.domain.Product import Product
from src.shared.Repository import Domain_Repository
from src.shared.UnitOfWork import UnitOfWork

class ProductCreate(ICommand):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
class ProductCreateHandler(ICommandHandler):
    def __init__(self, repo: Domain_Repository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow
    def handle(self, command: ProductCreate):
        product = Product.create(command.id, command.name, command.price)
        self.repo.save(product)
        self.uow.register(product)

class ProductActivate(ICommand):
    def __init__(self, id):
        self.id = id
class ProductActivateHandler(ICommandHandler):
    def __init__(self, repo: Domain_Repository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow
    def handle(self, command: ProductActivate):
        product: Product = self.repo.find(command.id)
        product.activate()
        self.repo.save(product)
        self.uow.register(product)


class ProductDiscontinue(ICommand):
    def __init__(self, id):
        self.id = id
class ProductDiscontinueHandler(ICommandHandler):
    def __init__(self, repo: Domain_Repository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow
    def handle(self, command: ProductDiscontinue):
        product: Product = self.repo.find(command.id)
        product.discontinued()
        self.repo.save(product)
        self.uow.register(product)


class ProductOutOfStack(ICommand):
    def __init__(self, id):
        self.id = id
class ProductOutOfStackHandler(ICommandHandler):
    def __init__(self, repo: Domain_Repository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow
    def handle(self, command: ProductOutOfStack):
        product: Product = self.repo.find(command.id)
        product.outofstack()
        self.repo.save(product)
        self.uow.register(product)

