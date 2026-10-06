from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_has_app_name() -> None:
    response = client.get("/info")
    assert response.status_code == 200
    assert "app" in response.json()
