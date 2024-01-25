from datetime import datetime

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.log.structured_logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    "Request logging middleware."

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        start = datetime.now()
        response = await call_next(request)

        logger.info(
            "incoming request",
            extra={
                "req": {
                    "method": request.method,
                    "url": request.url.path,
                    "client_address": f"{request.client.host}:{request.client.port}",
                },
                "res": {
                    "status_code": response.status_code,
                    "duration_in_seconds": str(
                        (start - datetime.now()).total_seconds()
                    ),
                },
            },
        )

        return response
