from uuid import UUID

class OrderItem:
    def __init__(self, 
                 product_id: UUID, 
                 name: str,
                 price: int, 
                 quantity: int):
        self.product_id = product_id
        self.price = price
        self.name = name
        self.quantity = quantity

    @classmethod
    def create(cls, 
               product_id,
               name,
               price, 
               quantity):
        return cls(product_id,
                   name,
                   price, 
                   quantity)

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"OrderItems(product_id={self.product_id},name={self.name} price={self.price}, quantity={self.quantity})"
