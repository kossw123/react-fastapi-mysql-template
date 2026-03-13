from fastapi import FastAPI, APIRouter, Depends
from sqlmodel import Session
from src.Product.infra.product_repository import ProductRepository, ProductModel
from src.database import get_session

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductModel])
def read_products(session: Session = Depends(get_session)):
    repo = ProductRepository(session)
    return repo.get_all()

@router.post("/", response_model=ProductModel)
def create_product(product: ProductModel, session: Session = Depends(get_session)):
    repo = ProductRepository(session)
    return repo.create(product)


