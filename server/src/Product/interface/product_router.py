from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.Product.infra.product_repository import ProductRepository, ProductModel
from infra.database import get_session


from src.Product.application.ProductService import Temp_ProductService
from src.shared.CommandBus import CommandBus
from src.shared.EventDispatcher import EventDispatcher

from src.shared.Repository import InMemoryStore

import logging


router = APIRouter(prefix="/products", tags=["products"])



@router.get("/", response_model=list[ProductModel])
def read_products(session: Session = Depends(get_session)):
    repo = ProductRepository(session)
    return repo.get_all()

# @router.post("/", response_model=ProductModel)
# def create_product(product: ProductModel, session: Session = Depends(get_session)):
#     repo = ProductRepository(session)
#     return repo.create(product)


from src.Product.domain.Product import Product
from src.shared.UnitOfWork import UnitOfWork

def get_uow(session: Session = Depends(get_session)):
    return UnitOfWork(session)


# Toy
@router.post("/", response_model=ProductModel)
# fastapi는 들어온 데이터를 자동으로 파싱해준다.
# fastapi는 함수 시그니처를 보고 타입힌트가 있는 경우, 타입 힌트를 규칙으로 사용해서 강제 파싱을 해준다.
# response_model은 pydantic의 decorator로써 출력 데이터를 타입에 맞게 변환한다.
def create_product(product: ProductModel, session: Session = Depends(get_session)):

    bus = CommandBus()
    dispatcher = EventDispatcher()
    memory_store = InMemoryStore()

    db_session_repository = ProductRepository(session)
    uow = UnitOfWork(session)

    service = Temp_ProductService(
        bus,
        dispatcher,
        memory_store,
    )

    with uow:
        result = service.create_product(product, uow)
    
    # orm 형태로 바꾸지 않고 return을 해서 문제가 발생
    res = {
        "id": result.id,
        "name": result.name,
        "price": result.price,
        "status": result.status
    }
    
    return res


