import json
import logging
import os
from logging import Formatter


class JsonFormatter(Formatter):
    "Formats incomming log events into JSON."

    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record: dict):
        json_record = {}
        json_record["message"] = record.getMessage()

        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]

        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]

        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)

        return json.dumps(json_record)


logging.getLogger("uvicorn.access").disabled = True  # disable uvicorn log

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger = logging.root
logger.handlers = [handler]
logger.level = os.getenv("LOG_LEVEL", logging.INFO)


__all__ = ["logger"]
