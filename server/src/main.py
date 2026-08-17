from src.config import create_app
from infra.logging.loki_handler import LokiHandler
import logging

from src.config import create_app
from infra.logging.loki_handler import LokiHandler


loki_handler = LokiHandler(
    "http://loki:3100/loki/api/v1/push"
)

loki_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

loki_handler.setFormatter(formatter)

root_logger = logging.getLogger(__name__)
root_logger.setLevel(logging.INFO)
root_logger.addHandler(loki_handler)

logger = logging.getLogger(__name__)
logger.info("===== LOKI TEST ======")

app = create_app()