from sqlmodel import Session, select
from src.Product.infra.product_model import ProductModel

class ProductRepository():
    def __init__(self, session: Session):
        self.session = session
    def create(self, product: ProductModel):
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product
    def get_all(self):
        statement = select(ProductModel)
        return self.session.exec(statement).all()