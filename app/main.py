import logging

from fastapi import FastAPI

from app.routers.test_router import router as test_router
from app.sentry_init import init_sentry

logger = logging.getLogger(__name__)

# Ініціалізація Sentry
init_sentry()
logger.info("Sentry initialized")

app = FastAPI(title="Lab FastAPI Project")
app.include_router(test_router)

logger.info("FastAPI app initialized")
