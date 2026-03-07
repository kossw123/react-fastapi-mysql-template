from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session