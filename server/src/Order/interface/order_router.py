from typing import TYPE_CHECKING
from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from src.Order.application.OrderService import OrderService
from src.Order.infra.models.OrderRequest import OrderRequest
from src.Order.infra.models.OrderResponse import OrderResponse
from infra.database import verify_access_token
order_router = APIRouter(prefix="/order", tags=["order"], dependencies=[
    Depends(verify_access_token)
])

@order_router.post("/ordering")
def read_order(request: OrderRequest, 
               uow: UnitOfWork = Depends(get_uow)) -> OrderResponse:
    print("ROUTER ORDERING CALL")
    bus = container["COMMAND_BUS"]
    dispatcher = container["EVENT_DISPATCHER"]
    service = OrderService(bus, dispatcher, uow)
    return service.create_order(request)