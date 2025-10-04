from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_and_course_for_enrollment():
    client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    client.post("/courses/", json={"title": "Data Science", "description": "Intro to DS"})

def test_enroll_user():
    response = client.post("/enrollments/", json={"user_id": 2, "course_id": 3})
    assert response.status_code == 200
    assert response.json()["user_id"] == 2

def test_enroll_user_twice_should_fail():
    response = client.post("/enrollments/", json={"user_id": 2, "course_id": 3})
    assert response.status_code == 400

def test_mark_course_complete():
    response = client.put("/enrollments/1/complete")
    assert response.status_code == 200
    assert response.json()["completed"] is True

def test_get_user_enrollments():
    response = client.get("/enrollments/user/2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_all_enrollments():
    response = client.get("/enrollments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)