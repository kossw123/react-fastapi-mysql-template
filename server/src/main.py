from src.config import create_app
from src.toy_bootstrap import (
    global_config
    )

app = create_app()


config = global_config()
container = config.global_bootstrap()

config.product_create_command()


# command 등록까진 완료