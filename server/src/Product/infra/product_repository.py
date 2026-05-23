from abc import ABC, abstractmethod
from sqlmodel import select, delete
from src.Product.infra.product_model import ProductModel
from src.Product.domain.Product import Product

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlmodel import Session
    from uuid import UUID

class IProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        pass
    @abstractmethod
    def find(self, product_id: UUID) -> Product | None:
        pass
    @abstractmethod
    def delete(self, product_id: UUID):
        pass

class SqlAlchemy_ProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, product: Product) -> Product:

        mapper = _Mapper()
        orm = mapper._to_orm(product)
        print("[ProductModel PK: ]", orm.id)
        self.session.add(orm)
        self.session.flush()
        self.session.refresh(orm)
        return product

    def find(self, product_id: UUID) -> Product | None:
        mapper = _Mapper()
        statement = select(ProductModel).where(ProductModel.id == product_id)
        orm = self.session.exec(statement).first()

        if orm is None:
            raise Exception("[SqlAlchemy_ProductRepository.find] session.exec.fist() is null")
        else:
            print(f"[SqlAlchemy_ProductRepository.find] FIND PK is {orm.id}")
            product = mapper._to_domain(orm)
        return product

    def delete(self, product_id: UUID):
        statement = delete(ProductModel).where(ProductModel.id == product_id)
        self.session.exec(statement)

    def get_all(self):
        mapper = _Mapper()
        statement = select(ProductModel)
        orms = self.session.exec(statement).all()
        return [
            mapper._to_domain(orm)
            for orm in orms
        ]

    
class _Mapper():
    def _to_orm(self, product: Product) -> ProductModel:
        return ProductModel(
            id = product.id,
            name = product.name,
            price = product.price,
            status = product.status
        )
    def _to_domain(self, orm: ProductModel) -> Product:
        return Product.restore(
            id = orm.id,
            name = orm.name,
            price = orm.price,
            status = orm.status
        )