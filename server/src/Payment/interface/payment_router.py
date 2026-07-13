from typing import TYPE_CHECKING
from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.Payment.application.PaymentService import PaymentService
from src.Product.infra.product_repository import ProductModel
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from uuid import UUID
from infra.database import verify_access_token


payment_router = APIRouter(prefix="/payment", tags=["payment"], dependencies=[
    Depends(verify_access_token)
])


@payment_router.post("/", response_model=list[ProductModel])
def read_payment(uow: UnitOfWork = Depends(get_uow)):
        bus = container["COMMAND_BUS"]
        dispatcher = container["EVENT_DISPATCHER"]
        service = PaymentService(bus, dispatcher)

        # return 