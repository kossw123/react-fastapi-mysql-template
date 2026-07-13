from sqlmodel import Session
from src.Product.infra.product_repository import SqlAlchemy_ProductRepository
from infra.login.auth_repository import AuthRepository
from src.Order.infra.order_repository import OrderRepository
# Request 발생
# → UoW 생성
#     → Session 생성
#     → Repository 생성
# → Handler 실행
# → Commit/Rollback
# → Session 종료


class UnitOfWork:
    def __init__(self, session: Session):
        self.seen = set()
        self.session = session
        self.product_repository = SqlAlchemy_ProductRepository(session)
        self.order_repository = OrderRepository(session)
        self.auth_repository = AuthRepository(session)

    def domain_register(self, aggregate):
        self.seen.add(aggregate)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

    def collect_event(self):
        events = []
        for aggregate in self.seen:
            events.extend(aggregate.root.pull_events())

        return events
