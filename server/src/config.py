from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from src.database import engine
from fastapi.middleware.cors import CORSMiddleware
from src.Product.interface.product_router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://upgraded-space-adventure-967j956r9ggc7qqv-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)