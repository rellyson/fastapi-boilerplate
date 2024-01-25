from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.http import status

from .models import HealthResponse


async def check_health(req: Request) -> HealthResponse:
    return HealthResponse(
        message=status.STATUS_OK.name(),
        status=status.STATUS_OK.code(),
        timestamp=datetime.now(),
    )
