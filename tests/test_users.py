from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_user():
    response = client.put("/users/1", json={"name": "Alice Updated", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Updated"

def test_deactivate_user():
    response = client.put("/users/1/deactivate")
    assert response.status_code == 200
    assert response.json()["is_active"] is False

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"