from fastapi import Header, HTTPException
from sqlmodel import create_engine, Session
from .env_settings import settings
from src.shared.UnitOfWork import UnitOfWork
from infra.login.jwt_token import JwtTokenProvider

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



def verify_access_token(
    authorization: str = Header(None)
):
    print("VERIFY TOKEN")

    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    JwtTokenProvider().validate_access_token(
        token
    )