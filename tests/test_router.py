from fastapi import APIRouter
from fastapi.testclient import TestClient

from app.main import app

router = APIRouter()
client = TestClient(app)


@router.get("/sentry-debug-test")
def sentry_debug_test():
    response = client.get("/sentry-debug")

    expec_status = 500
    assert response.status_code == expec_status

    message = "Sentry " "test " "passed"

    return {"message": message}
