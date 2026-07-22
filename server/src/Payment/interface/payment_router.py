from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.Payment.application.PaymentService import PaymentService
from src.Product.infra.product_repository import ProductModel
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from infra.database import verify_access_token
from server.src.Payment.infra.models.PaymentConfirmRequest import PaymentConfirmRequest


payment_router = APIRouter(prefix="/payment", tags=["payment"], dependencies=[
    Depends(verify_access_token)
])


@payment_router.post("/confirm")
def confirm(request: PaymentConfirmRequest, 
                    uow: UnitOfWork = Depends(get_uow)):
        print("confirm 진입")
        print(f"data : {request}")
        bus = container["COMMAND_BUS"]
        dispatcher = container["EVENT_DISPATCHER"]
        service = PaymentService(bus, dispatcher)

        return service.confirm(request, uow)