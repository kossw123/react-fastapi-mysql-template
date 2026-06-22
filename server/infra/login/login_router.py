from typing import TYPE_CHECKING
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from infra.database import get_uow
from infra.login.AuthService import AuthService
from infra.login.models.LoginRequest import LoginRequest
from infra.login.models.SignUpRequest import SignUpRequest
from http import HTTPStatus
if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork


auth_router = APIRouter(prefix="/auth", tags=["login"])

# Sign up
@auth_router.post("/signup")
def sign_up(request: SignUpRequest, 
            uow: UnitOfWork = Depends(get_uow)):

    service = AuthService()
    service.create_account(request.username, 
                           request.email, 
                           request.password, 
                           uow)


# Login
@auth_router.post("/login")
def login(login_data: LoginRequest,
          response: Response,
          uow: UnitOfWork = Depends(get_uow)):
    service = AuthService()
    return service.login(login_data, response, uow)


# Logout
# @auth_router.get("/logout")
# def logout():

from infra.login.models.UserRequest import UserRequest

@auth_router.post("/getuser")
def get_current_user(target_data: UserRequest,
                     uow: UnitOfWork = Depends(get_uow)):
    service = AuthService()
    return service.find_user(target_data, uow)



# 1. 로그인 성공 시 JWT 발급
# 2. localStorage에 저장 
# # 3. ProductedRoute 추가
# 4. 로그아웃 시 토큰 삭제 + 로그인 페이지 이동
# 5. FastAPI에 /auth/logout 추가



@auth_router.post("/refresh")
def refresh_access_token(request: Request, 
                         response: Response):
    print("ROUTER REFRESH CALL")
    refresh_token = request.cookies.get("refresh_token")
    
    service = AuthService()
    return service.refresh(refresh_token)