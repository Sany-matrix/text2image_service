from fastapi.testclient import TestClient
from app.main import app, get_generator
import pytest

client = TestClient(app)

def test_generate_image_empty():
    response = client.post("/generate-image/", json= {"text": ""})
    assert response.status_code == 400


def test_generate_image_valid(monkeypatch):
    def mock_generate(prompt):
        print("MOCK CALLED!")
        return "http://test-image.com/sample.png"
    
    app.dependency_overrides[get_generator] = lambda: mock_generate

    response = client.post("/generate-image/", json={"text": "a cat on Mars"})
    assert response.status_code == 200
    assert "image_url" in response.json()

