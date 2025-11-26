import logging

import sentry_sdk

logger = logging.getLogger(__name__)


def broken_function():
    try:
        raise Exception("Test Sentry error: onboarding check")
    except Exception as e:
        logger.error(f"[FAKE_SERVICE] Error occurred: {e}")
        sentry_sdk.capture_exception(e)
        raise
