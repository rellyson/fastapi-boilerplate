from app.core.http.handlers.exception_handlers import (
    internal_server_exception_handler,
    not_found_exception_handler,
)
from app.core.http.status import STATUS_INTERNAL_SERVER_ERROR, STATUS_NOT_FOUND

config = {
    "title": "FastAPI Boilerplate",
    "description": """
This project provides a basic configured FastAPI
that can be used in RESTFul API applications.

You can find more info about FastAPI at the
[Official Documentation](https://fastapi.tiangolo.com/]). 
""",
    "docs_url": "/docs",
    "redoc_url": None,
    "exception_handlers": {
        STATUS_NOT_FOUND.code(): not_found_exception_handler,
        STATUS_INTERNAL_SERVER_ERROR.code(): internal_server_exception_handler,
    },
}
