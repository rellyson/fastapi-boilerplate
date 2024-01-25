from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.http.errors import (
    BaseHTTPError,
    HTTPInternalServerError,
    HTTPNotFoundError,
)


def default_http_error_handler(req: Request, exc: BaseHTTPError):
    "Handles raised BaseHTTPError and returns a HTTP Error"

    return JSONResponse(exc.to_json(), exc.status_code)


def not_found_exception_handler(req: Request, exc: Exception):
    "Handles not found routes and returns a HTTP Error"

    error = HTTPNotFoundError(f"Resource not found: {req.method} {req.url.path}")

    return JSONResponse(content=error.to_json(), status_code=error.status_code)


def internal_server_exception_handler(req: Request, exc: Exception):
    "Handles internal errors and returns a HTTP Error"

    error = HTTPInternalServerError("An internal error has occurred. Try again later")

    return JSONResponse(content=error.to_json(), status_code=error.status_code)
