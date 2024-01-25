from datetime import datetime

from app.core.http.status import *


class BaseHTTPError(Exception):
    """
    A HTTP Error represents that something went wrong during request.
    """

    def __init__(self, name: str, message: str, status_code: int):
        self.name = name
        self.message = message
        self.status_code = status_code

    def to_json(self):
        "Serializes to JSON format."

        return {
            "error": self.name,
            "message": self.message,
            "status_code": self.status_code,
            "timestamp": datetime.now().isoformat(),
        }


class HTTPBadRequestError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(STATUS_BAD_REQUEST.name(), message, STATUS_BAD_REQUEST.code())


class HTTPUnauthorizedError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(
            STATUS_UNAUTHORIZED.name(), message, STATUS_UNAUTHORIZED.code()
        )


class HTTPForbiddenError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(STATUS_FORBIDDEN.name(), message, STATUS_FORBIDDEN.code())


class HTTPNotFoundError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(STATUS_NOT_FOUND.name(), message, STATUS_NOT_FOUND.code())


class HTTPConflictError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(STATUS_CONFLICT.name(), message, STATUS_CONFLICT.code())


class HTTPInternalServerError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(
            STATUS_INTERNAL_SERVER_ERROR.name(),
            message,
            STATUS_INTERNAL_SERVER_ERROR.code(),
        )


class HTTPNotImplementedError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(
            STATUS_NOT_IMPLEMENTED.name(),
            message,
            STATUS_NOT_IMPLEMENTED.code(),
        )


class HTTPServiceUnavailableError(BaseHTTPError):
    def __init__(self, message: str):
        super().__init__(
            STATUS_SERVICE_UNAVAILABLE.name(),
            message,
            STATUS_SERVICE_UNAVAILABLE.code(),
        )
