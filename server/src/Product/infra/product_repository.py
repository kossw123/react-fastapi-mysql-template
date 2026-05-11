from src.shared_interface.ISessionRepository import ISessionRepository
from sqlmodel import select
from src.Product.infra.product_model import ProductModel

class ProductRepository(ISessionRepository):

    def add_session(self, product: ProductModel):
        self.session.add(product)
        return product

    def get_all(self):
        statement = select(ProductModel)
        return self.session.exec(statement).all()



