from sqlmodel import create_engine, Session
from .env_config import settings

# codespace
# DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

# Project IDX
DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session