from sqlmodel import Session

class UnitOfWork():
    def __init__(self, session: Session):
        self.seen = set()
        # 이건 get_session을 의미한다.
        # 그렇다면 ProductRepository의 add와 commit은?
        # product를 받아야 한다.
        self.session = session

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


from src.Product.infra.product_repository import ProductRepository

class Toy_UnitOfWork():
    def __init__(self, session: Session):
        self.seen = set()
        self.session = session
        self.product_repository = ProductRepository(session)

    def domain_register(self, aggregate):
        self.seen.add(aggregate)

    def __enter__(self):
        self.product_repository.add_session(self.session)
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
