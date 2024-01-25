import os

from fastapi import FastAPI

from app.config.app_config import config
from app.core.http.middlewares import logging
from app.routers import health


def bootstrap():
    """Creates an ASGI-compliant application."""

    app = FastAPI(**config)
    app.add_middleware(logging.LoggingMiddleware)
    app.include_router(health.router)

    return app
