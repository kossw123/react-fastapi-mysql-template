from sqlmodel import create_engine, Session
from src.env_settings import settings

# e.g
# DATABASE_URL = mysql+pymysql://<username>:<password>@<host>:<port>/<database>

# codespace
# DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

# local
# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testdb"
DATABASE_URL = settings.database_url


engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session