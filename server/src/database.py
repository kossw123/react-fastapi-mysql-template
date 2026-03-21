from sqlmodel import create_engine, Session

# codespace
# DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

# Project IDX
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/testdb"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session