
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from sqlmodel import Session, select

if TYPE_CHECKING:
    from infra.login.UserModel import UserModel
    from src.shared.UnitOfWork import UnitOfWork


class IAuthRepository(ABC):
    @abstractmethod
    def insert(self, 
               data: UserModel):
        pass


class SignUp_Repository(IAuthRepository):
    def __init__(self, 
                 session: Session):
        self.session = session

    
    def save(self, product: Product) -> Product:

        mapper = _Mapper()
        orm = mapper._to_orm(product)
        print("[ProductModel PK: ]", orm.id)
        self.session.add(orm)
        self.session.flush()
        self.session.refresh(orm)
        return product


    def insert(self,
               data: UserModel,
               uow: UnitOfWork) -> UserModel:
        orm = data
        self.session.add(orm)
        self.session.flush()
        self.session.refresh(orm)
        return orm