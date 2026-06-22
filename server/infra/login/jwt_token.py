from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from http import HTTPStatus
class JwtTokenProvider:
    SECRET_KEY = "my-secret-key"
    ALGORITHM = "HS256"

    def create_access_token(self, 
                            username: str,
                            expire_delta: timedelta = None) -> str:
        _to_payload = { 
            "username": username
        }

        if expire_delta:
            expire = datetime.now(timezone.utc) + expire_delta
        else:
            expire = datetime.new(timezone.utc) + timedelta(minutes=3)

        _to_payload.update({
            "exp": expire,
            "token_type": "access"
        })

        return jwt.encode(_to_payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
    

    def validate_access_token(self,
                              token: str) -> dict:
        try:
            payload = jwt.decode(token, self.SECRET_KEY, self.ALGORITHM)
            if payload.get("token_type") != "access":
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail="not verify access token"
                )
        except JWTError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="JWT Token UnAuthorized"
            )
        
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="expire JWT Token"
            ) 

        return payload
    
    def validate_refresh_token(self,
                              token: str) -> dict:
            print("VALIDATE REFRESH TOKEN CALL")
            print("TOKEN = ", token)
            try:
                payload = jwt.decode(token, self.SECRET_KEY, self.ALGORITHM)
                if payload.get("token_type") != "refresh":
                    raise HTTPException(
                        status_code=HTTPStatus.UNAUTHORIZED,
                        detail="not verify access token"
                    )
                
                print("PAYLOAD = ", payload)
                
            except ExpiredSignatureError:
                print("REFRESH TOKEN EXPIRE")
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail="expire JWT Token"
                ) 
            except JWTError as e:
                print("JWT ERROR =", e)
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail="JWT Token UnAuthorized"
                )
            
            

            return payload



    def create_refresh_toekn(self,
                             username: str,
                             expire_delta) -> str:
        _to_payload = dict(username=username)

        if expire_delta:
            expire = datetime.now(timezone.utc) + expire_delta
        else:
            expire = datetime.new(timezone.utc) + timedelta(minutes=3)

        _to_payload.update({
            "exp": expire,
            "token_type": "refresh"
        })

        return jwt.encode(_to_payload, self.SECRET_KEY, self.ALGORITHM)