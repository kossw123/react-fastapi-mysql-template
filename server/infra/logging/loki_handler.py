import logging
import time
import requests
class LokiHandler(logging.Handler):

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def emit(self, record: logging.LogRecord):
        try:
            print("🔥 LOKI HANDLER CALLED")

            log_entry = self.format(record)

            payload = {
                "streams": [
                    {
                        "stream": {
                            "service": "fastapi",
                            "level": record.levelname,
                        },
                        "values": [
                            [
                                str(time.time_ns()),
                                log_entry,
                            ]
                        ],
                    }
                ]
            }

            print("🔥 LOKI PAYLOAD:", payload)

            response = requests.post(
                self.url,
                json=payload,
                timeout=1,
            )

            print("🔥 LOKI RESPONSE:", response.status_code, response.text)

            response.raise_for_status()

        except Exception:
            self.handleError(record)