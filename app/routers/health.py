from datetime import datetime

from fastapi import APIRouter

from app.core.health import handlers
from app.core.health.models import HealthResponse
from app.core.http.methods import METHOD_GET

router = APIRouter(prefix="/v1/health")

router.add_api_route(
    "",
    handlers.check_health,
    methods=[METHOD_GET],
    tags=["health"],
    response_model=HealthResponse,
)
