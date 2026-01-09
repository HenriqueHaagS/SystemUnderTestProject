from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_not_found():
    response = client.get("/nonexistent")
    assert response.status_code == 404

def test_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 404
