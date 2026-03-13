from src.shared.AggregateRoot import AggregateRoot
from src.Product.domain.events import *
from src.Product.domain.ProductStatus import ProductStatus

class Product():
    def __init__(self, id, name, price):
        self.root = AggregateRoot()
        self.product_id = id
        self.product_name = name
        self.product_price = price
        self.product_status = ProductStatus.DRAFT
    
    @classmethod
    def create(cls, id, name, price):
        if not name:
            raise Exception("Required Product Name")
        if not price:
            raise Exception("Required Product Price")
        
        instance = cls(id, name, price)
        instance.root.register(
            ProductCreated(
                instance.product_id,
                instance.product_name,
                instance.product_price
            ))
        return instance


    def activate(self):
        if self.product_status == ProductStatus.ACTIVE:
            return
        if self.product_status == ProductStatus.DISCONTINUED:
            raise Exception("Product is Disconitnued")
        if self.product_status == ProductStatus.OUTOFSTOCK:
            raise Exception("Product is out of stack")

        self.product_status = ProductStatus.ACTIVE
        self.root.register(ProductActivated(self.product_id))

    def discontinued(self):
        if self.product_status == ProductStatus.DISCONTINUED:
            return
        if self.product_status == ProductStatus.OUTOFSTOCK:
            raise Exception("Product Already out of stack")
        
        self.product_status = ProductStatus.DISCONTINUED
        self.root.register(ProductDiscontinued(self.product_id, self.product_name))

    def outofstack(self):
        if self.product_status == ProductStatus.OUTOFSTOCK:
            return
        
        self.product_status = ProductStatus.OUTOFSTOCK
        self.root.register(ProductOutOfStack(self.product_id, self.product_name))
