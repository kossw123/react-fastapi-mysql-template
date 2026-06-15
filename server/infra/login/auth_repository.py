from sqlmodel import Session, select

from infra.login.models.UserModel import UserModel

class AuthRepository():
    def __init__(self,
                 session: Session):
        self.session = session
    def save(self,
             user: UserModel) -> UserModel:
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)

        return user
    
    def find_by_name(self,
                     username: str) -> UserModel:
        stmt = select(UserModel).where(UserModel.username == username)
        orm = self.session.exec(stmt).first()
        
        if orm is None:
            return None
        
        return orm