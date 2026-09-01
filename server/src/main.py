from src.config import create_app
from infra.logging.loki_handler import LokiHandler
import logging

from src.config import create_app
from infra.logging.loki_handler import LokiHandler

def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    loki_handler = LokiHandler("http://loki:3100/loki/api/v1/push")
    loki_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    loki_handler.setFormatter(formatter)

    if not root_logger.handlers:
        root_logger.addHandler(loki_handler)


setup_logging()

logger = logging.getLogger(__name__)
logger.info("===== LOKI TEST ======")
logger.info("===== GRAFANA CONNECTION ======")
app = create_app()