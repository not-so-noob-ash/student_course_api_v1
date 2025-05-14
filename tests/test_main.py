from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "Test User", "email": "testuser@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_create_course():
    response = client.post("/courses/", json={"title": "Science", "description": "Science course"})
    assert response.status_code == 200
    assert response.json()["title"] == "Science"