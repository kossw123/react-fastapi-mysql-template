from abc import ABC, abstractmethod
from sqlmodel import select, delete
from src.Product.infra.product_model import ProductModel
from src.Product.domain.Product import Product
from sqlalchemy import update
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

    def find_orm(self, 
                 product_id: UUID) -> ProductModel | None:
        statement = select(ProductModel).where(ProductModel.id == product_id)
        orm = self.session.exec(statement).first()

        if orm is None:
            raise Exception("[SqlAlchemy_ProductRepository.find] session.exec.fist() is null")
        else:
            print(f"[SqlAlchemy_ProductRepository.find] FIND PK is {orm.id}")
        return orm

    def get_all(self):
        mapper = _Mapper()
        statement = select(ProductModel)
        orms = self.session.exec(statement).all()
        return [
            mapper._to_domain(orm)
            for orm in orms
        ]

    def update(self, 
               product_id: UUID,
               product_data: ProductModel):
        mapper = _Mapper()
        
        orm = self.find_orm(product_id)
        print(f"[product_repository.update] target data : {product_data.name}")

        # Core Update function, InCorrect method
        # statement = update(ProductModel).where(ProductModel.id == orm.id).values(
        #     name = product_data.name,
        #     price = product_data.price
        # )
        # self.session.exec(statement)

        orm.name =  product_data.name
        orm.price = product_data.price

        self.session.flush()
        self.session.refresh(orm)
        return mapper._to_domain(orm)

    
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