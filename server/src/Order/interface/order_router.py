from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from src.Order.application.OrderService import OrderService
from src.Order.infra.models.OrderRequest import OrderRequest
from src.Order.infra.models.OrderResponse import OrderResponse
from infra.database import verify_access_token
from src.Order.infra.order_model import OrderModel
from uuid import UUID

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


# const orderResponse = await axiosinstance.get(`/orders/${orderId}`);
@order_router.get("/{order_id}", response_model=OrderModel) 
def find_order(order_id: UUID, 
               uow: UnitOfWork = Depends(get_uow)) -> OrderResponse:
    bus = container["COMMAND_BUS"]
    dispatcher = container["EVENT_DISPATCHER"]
    
    service = OrderService(bus, dispatcher, uow)
    return service.find_by_id(order_id)