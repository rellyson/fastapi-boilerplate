from datetime import datetime

from pydantic import BaseModel


class HealthResponse(BaseModel):
    "Health check response Model."

    message: str
    status: int
    timestamp: datetime
