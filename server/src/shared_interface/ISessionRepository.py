from abc import ABC
from sqlmodel import Session

class ISessionRepository(ABC):
    def __init__(self, session: Session):
        self.session = session