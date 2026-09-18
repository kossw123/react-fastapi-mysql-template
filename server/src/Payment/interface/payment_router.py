import os
from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.Payment.application.PaymentService import PaymentService
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from infra.database import verify_access_token
from src.Payment.infra.models.PaymentConfirmRequest import PaymentConfirmRequest
from src.Payment.infra.TossPaymentClient import TossPaymentClient


payment_router = APIRouter(prefix="/payment", tags=["payment"], dependencies=[
    Depends(verify_access_token)
])


@payment_router.post("/confirm")
def confirm(request: PaymentConfirmRequest, 
                    uow: UnitOfWork = Depends(get_uow)):
        print(f"data : {request}")
        bus = container["COMMAND_BUS"]
        dispatcher = container["EVENT_DISPATCHER"]
        toss_client = TossPaymentClient(
                secret_key=os.environ("TOSS_SECRET_KEY")
        )
        service = PaymentService(bus, dispatcher, uow, toss_client)

        return service.confirm(request)