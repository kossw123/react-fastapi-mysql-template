from sqlmodel import create_engine, Session


# e.g
# DATABASE_URL = mysql+pymysql://<username>:<password>@<host>:<port>/<database>

# codespace
# DATABASE_URL = "mysql+pymysql://user:password@mysql/testdb"

# local
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testdb"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session