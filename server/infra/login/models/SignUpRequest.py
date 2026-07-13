from pydantic import BaseModel, model_validator

class SignUpRequest(BaseModel):
    username: str
    email: str
    password: str
        
    @model_validator(mode='after')
    def verify_credentials(self):
        if self.username is None and self.email is None and self.password is None:
            raise ValueError("모든 인증 정보가 비어있을 수 없습니다.")
        return self
