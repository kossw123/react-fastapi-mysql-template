from typing import TYPE_CHECKING
from fastapi import APIRouter, Depends
from infra.database import get_uow
from src.Product.application.ProductService import ProductService
from src.Product.infra.product_repository import ProductModel
from src.shared.UnitOfWork import UnitOfWork
from src.toy_bootstrap import container
from uuid import UUID
from infra.database import verify_access_token

if TYPE_CHECKING:
    from src.Product.domain.Product import Product

router = APIRouter(prefix="/products", tags=["products"], dependencies=[
    Depends(verify_access_token)
])


@router.get("/", response_model=list[ProductModel])
def read_products(uow: UnitOfWork = Depends(get_uow)):
    return uow.product_repository.get_all()


@router.post("/", response_model=ProductModel)
# fastapi는 들어온 데이터를 자동으로 파싱해준다.
# fastapi는 함수 시그니처를 보고 타입힌트가 있는 경우, 타입 힌트를 규칙으로 사용해서 강제 파싱을 해준다.
# response_model은 pydantic의 decorator로써 출력 데이터를 타입에 맞게 변환한다.
def create_product(product: ProductModel, uow: UnitOfWork = Depends(get_uow)):
    bus = container["COMMAND_BUS"]
    dispatcher = container["EVENT_DISPATCHER"]
    service = ProductService(bus, dispatcher)
    return service.create_product(product, uow)

# const res = await axios.delete(`${API}/products/${productId}`);
@router.delete("/{product_id}")
def deactivate_product(product_id: UUID, uow: UnitOfWork = Depends(get_uow)):
    bus = container["COMMAND_BUS"]
    dispatcher = container["EVENT_DISPATCHER"]
    
    service = ProductService(bus, dispatcher)
    service.discontinued_product(product_id, uow)
        


# const res = await axios.put(`${API}/products/${productId}`, updatedData);
@router.put("/{product_id}", response_model = ProductModel)
def update_product(product_id: UUID, 
                   product_data: ProductModel,
                   uow: UnitOfWork = Depends(get_uow)):
    bus = container["COMMAND_BUS"]
    dispatcher = container["EVENT_DISPATCHER"]    
    service = ProductService(bus, dispatcher)
    return service.update_product(product_id, product_data, uow)


