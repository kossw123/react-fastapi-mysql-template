from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from src.database import engine, get_session
from src.product_model import ProductModel
from src.product_repository import ProductRepository
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://upgraded-space-adventure-967j956r9ggc7qqv-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/products", response_model=list[ProductModel])
def read_products(session: Session = Depends(get_session)):
    repo = ProductRepository(session)
    return repo.get_all()

@app.post("/products", response_model=ProductModel)
def create_product(product: ProductModel, session: Session = Depends(get_session)):
    repo = ProductRepository(session)
    return repo.create(product)