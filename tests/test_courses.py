from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course():
    response = client.post("/courses/", json={"title": "Python Basics", "description": "Learn Python"})
    assert response.status_code == 200
    assert response.json()["title"] == "Python Basics"

def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_course_by_id():
    response = client.get("/courses/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2

def test_update_course():
    response = client.put("/courses/2", json={"title": "Python Advanced", "description": "Deep dive"})
    assert response.status_code == 200
    assert response.json()["title"] == "Python Advanced"

def test_close_enrollment():
    response = client.put("/courses/2/close")
    assert response.status_code == 200
    assert response.json()["is_open"] is False

def test_delete_course():
    response = client.delete("/courses/2")
    assert response.status_code == 200
    assert response.json()["message"] == "Course deleted"