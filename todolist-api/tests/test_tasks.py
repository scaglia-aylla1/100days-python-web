import pytest
from app import create_app
from app.extensions import db


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_task(client):
    response = client.post("/tasks/", json={
        "title": "Test Task"
    })

    assert response.status_code == 201
    data = response.get_json()

    assert data["title"] == "Test Task"
    assert data["completed"] is False


def test_get_tasks(client):
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.get_json()

    assert len(data) == 2


def test_update_task(client):
    response = client.post("/tasks/", json={"title": "Task para completar"})
    task_id = response.get_json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={
        "completed": True
    })

    assert response.status_code == 200

    data = response.get_json()
    assert data["completed"] is True


def test_delete_task(client):
    response = client.post("/tasks/", json={"title": "Task para deletar"})
    task_id = response.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204


def test_health_check(client):
    response = client.get("/tasks/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"