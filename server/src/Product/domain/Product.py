from typing import TYPE_CHECKING
from src.shared.AggregateRoot import AggregateRoot
from src.Product.domain.events import (
    ProductCreated,
    ProductActivated,
    ProductDiscontinued,
    ProductOutOfStack,
)
from src.Product.domain.ProductStatus import ProductStatus

if TYPE_CHECKING:
    from uuid import UUID


class Product:
    def __init__(self, id, name, price):
        self.root = AggregateRoot()
        self.id: UUID = id
        self.name: str = name
        self.price: int = price
        self.status: str = ProductStatus.DRAFT

    @classmethod
    def create(cls, id, name, price):
        if not name:
            raise Exception("Required Product Name")
        if not price:
            raise Exception("Required Product Price")

        instance = cls(id, name, price)
        instance.root.register(
            ProductCreated(instance.id, instance.name, instance.price)
        )
        return instance

    @classmethod
    def restore(cls, id, name, price, status):
        instance = cls(id, name, price)
        instance.status = status
        return instance

    def activate(self):
        if self.status == ProductStatus.ACTIVE:
            return
        if self.status == ProductStatus.DISCONTINUED:
            raise Exception("Product is Disconitnued")
        if self.status == ProductStatus.OUTOFSTOCK:
            raise Exception("Product is out of stack")

        self.status = ProductStatus.ACTIVE
        self.root.register(ProductActivated(self.id))

    def discontinued(self):
        if self.status == ProductStatus.DISCONTINUED:
            return
        if self.status == ProductStatus.OUTOFSTOCK:
            raise Exception("Product Already out of stack")

        self.status = ProductStatus.DISCONTINUED
        self.root.register(ProductDiscontinued(self.id, self.name))

    def outofstack(self):
        if self.status == ProductStatus.OUTOFSTOCK:
            return

        self.status = ProductStatus.OUTOFSTOCK
        self.root.register(ProductOutOfStack(self.id, self.name))
