from typing import TYPE_CHECKING
from fastapi import APIRouter, Depends
from infra.database import get_auth_uow
from infra.login.UserModel import UserModel
from src.shared.UnitOfWork import Auth_UnitOfWork
from src.toy_bootstrap import auth_container
from uuid import UUID

router = APIRouter(prefix="", tags={"login"})


# def create_product(product: ProductModel, uow: UnitOfWork = Depends(get_uow)):
#     bus = container["COMMAND_BUS"]
#     dispatcher = container["EVENT_DISPATCHER"]
#     service = ProductService(bus, dispatcher)

#     with uow:
#         result = service.create_product(product, uow)
#     return _to_response(result)


# Sign up
@router.post("/signup", response_model=UserModel)
def sign_up(data: UserModel, 
            uow: Auth_UnitOfWork = Depends(get_auth_uow)):
    repo = auth_container["SIGNUP_REPOSITORY"]
    with uow:
        repo.insert(data) 
    res = {
        "id": data.id,
        "name": data.name
    }
    return res


# login
# @router.post("/", response_model=LoginModel)