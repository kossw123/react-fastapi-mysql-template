from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from infra.database import engine
from fastapi.middleware.cors import CORSMiddleware
from src.Order.interface.order_router import order_router
from src.Product.interface.product_router import router
from infra.login.login_router import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    app.include_router(auth_router)
    app.include_router(order_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://upgraded-space-adventure-967j956r9ggc7qqv-3000.app.github.dev",
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
