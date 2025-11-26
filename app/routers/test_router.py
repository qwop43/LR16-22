import logging

import sentry_sdk
from fastapi import APIRouter, HTTPException

from app.services.fake_service import broken_function

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/sentry-debug")
async def trigger_error():
    logger.info("Trigger /sentry-debug called")
    try:
        broken_function()
    except Exception as e:
        logger.error("Error captured and sent to Sentry: %s", e)
        sentry_sdk.capture_exception(e)
        raise HTTPException(status_code=500, detail="Triggered Sentry test error")
    return {"status": "ok"}
