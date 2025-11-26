from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sentry_debug_route():
    response = client.get("/sentry-debug")
    assert response.status_code == 500
    assert response.json()["detail"] == "Triggered Sentry test error"
