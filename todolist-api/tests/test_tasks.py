import pytest
from app import create_app, db

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
    # cria task
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.get_json()

    assert len(data) == 2

def test_get_task_by_id(client):
    # cria task
    response = client.post("/tasks/", json={"title": "Task única"})
    task_id = response.get_json()["id"]

    # busca por id
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.get_json()

    assert data["id"] == task_id
    assert data["title"] == "Task única"

def test_update_task(client):
    # cria task
    response = client.post("/tasks/", json={"title": "Antigo"})
    task_id = response.get_json()["id"]

    # atualiza
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Novo",
        "completed": True
    })

    assert response.status_code == 200
    data = response.get_json()

    assert data["title"] == "Novo"
    assert data["completed"] is True

def test_delete_task(client):
    # cria task
    response = client.post("/tasks/", json={"title": "Para deletar"})
    task_id = response.get_json()["id"]

    # deleta
    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    # confirma que não existe mais
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404