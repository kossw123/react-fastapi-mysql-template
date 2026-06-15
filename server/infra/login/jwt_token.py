from jose import jwt
from datetime import datetime, timedelta

class JwtTokenProvider:
    SECRET_KEY = "my-secret-key"
    ALGORITHM = "HS256"

    def create_access_token(self, 
                            username: str) -> str:
        payload = {
            "username": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }

        return jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm=self.ALGORITHM
        )
    

    def validate_access_token(self,
                              token: str):
        return jwt.decode(token, self.SECRET_KEY, self.ALGORITHM)