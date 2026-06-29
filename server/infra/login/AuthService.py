from typing import TYPE_CHECKING
from infra.login.models.UserModel import UserModel
from fastapi import HTTPException
from infra.login.jwt_token import JwtTokenProvider
from infra.login.password_hasher import PasswordHasher
from uuid import UUID, uuid4
from datetime import timedelta
from infra.redis_client import blacklist_token
if TYPE_CHECKING:
    from src.shared.UnitOfWork import UnitOfWork
    from infra.login.models.LoginRequest import LoginRequest
    from infra.login.models.UserRequest import UserRequest
    from infra.login.models.UserResponse import UserResponse
    from fastapi import Response

class AuthService():
    def __init__(self):
        self.token_provider = JwtTokenProvider()
        self.password_hasher = PasswordHasher()        

    def create_account(self, 
                       username: str,
                       email: str,
                       password: str,
                       uow: UnitOfWork) -> UserModel:
        
        user_model = _Mapper()._to_usermodel(self.password_hasher, username, email, password)

        with uow:
            existing_user = uow.auth_repository.find_by_name(username)

            if existing_user:
                raise HTTPException(
                    status_code=409,
                    detail="이미 가입된 회원입니다."
                )
            uow.auth_repository.save(user_model)

        return user_model

    def login(self,
                     user: LoginRequest,
                     response: Response,
                     uow: UnitOfWork):
        
            with uow:
                account = uow.auth_repository.find_by_name(user.username)

            if account is None:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid username"
                )
            
            if self.password_hasher.verify(
                                        user.password, 
                                        account.password) is False:
                raise HTTPException(
                    status_code=401,
                    detail="Not verify password"
                )
            
            access_token = self.token_provider.create_access_token(account.username, expire_delta=timedelta(seconds=30))
            refresh_token = self.token_provider.create_refresh_toekn(account.username, expire_delta=timedelta(minutes=2))

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,    # secure=True는 HTTPS 환경에서만 킨다. HTTPS 환경이 아니면 쿠키를 가차없이 버린다는 설정이다.
                samesite="lax"
            )

            return {
                "token": access_token,
                "bearer": "bearer",
            }
                
    
    def find_user(self,
                  user: UserRequest,
                  uow: UnitOfWork) -> UserResponse:

        if user.username is None:
            raise HTTPException(
                status_code="400",
                detail="not input username"
            )

        account = uow.auth_repository.find_by_name(user.username)

        if account is None:
            raise HTTPException(
                status_code="401",
                detail="not found user"
            ) 

        return _Mapper()._to_userresponse(user)

    def refresh(self,
                token: str):
        print("AUTHSERVICE REFRESH CALL")
        payload = self.token_provider.validate_refresh_token(token)

        username= payload["username"]
        
        access_token = self.token_provider.create_access_token(username, expire_delta=timedelta(seconds=30))
        return {
            "token": access_token,
            "bearer": "bearer",
        }
    

    def logout(self,
               token: str):
        print("CALL AUTHSERVICE.LOGOUT")
        payload = self.token_provider.validate_access_token(token)
        
        jti = payload.get("jti")
        expire=  payload.get("exp")

        blacklist_token(jti, expire)


class _Mapper():
    def _to_usermodel(self,
                      hasher: PasswordHasher,
                      username: str,
                      email: str,
                      password: str) -> UserModel:
        id: UUID = uuid4()
        return UserModel(
            id = id,
            username = username,
            email =  email,
            password = hasher.hash(password)
        )
    
    def _to_userresponse(self,
                        user: UserRequest) -> UserResponse:
        return UserResponse(
            user.username
        )