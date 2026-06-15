from sqlmodel import create_engine, Session
from .env_settings import settings
from src.shared.UnitOfWork import UnitOfWork

# e.g
# DATABASE_URL = mysql+pymysql://<username>:<password>@<host>:<port>/<database>

# codespace
# DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

# local
# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testdb"
DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

def get_uow():
    with Session(engine) as session:
        yield UnitOfWork(session)

        