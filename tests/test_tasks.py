# импортируем FastAPI приложение

import pytest

from app.main import app

# TestClient — инструмент для тестирования API
from fastapi.testclient import TestClient

# создаём клиент для тестов
client = TestClient(app)

@pytest.fixture
def created_task(client)

def test_create_task():
    response = client.post(
        "tasks",
        json={
            "title": "test task",
            "description": "test description"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "test task"
    assert data["description"] == "test description"
    assert "id" in data


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id():
    create = client.post("/tasks", json={
            "title": "task1",
            "description": "desc"
        })

    task_id = create.json()["id"]
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_delete_task():
    create = client.post("/tasks", json={
        "title": "task2",
        "description": "desc"
    })

    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    get = client.get(f"/tasks/{task_id}")
    assert get.status_code == 404


def test_create_task_invalid():
    response = client.post("/tasks", json={})

    assert response.status_code == 422


def test_create_task_missing_title():
    create = client.post("/tasks", json={
        "description": "desc"
    })

    assert create.status_code == 422


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_delete_missing_task():
    response = client.delete("/tasks/999")

    assert response.status_code == 400


def test_task_is_really_deleted():
    create = client.post("/tasks", json={
        "title": "temp",
        "description": "temp"
    })

    task_id = create.json()["id"]

    client.delete(f"/tasks/{task_id}")

    get = client.get(f"/tasks/{task_id}")

    assert get.status_code == 404


def test_tasks_list_increases():
    initial = client.get("/tasks").json()
    initial_len = len(initial)

    client.post("/tasks", json={
        "title": "new task",
        "description": "desc"
    })

    after = client.get("/tasks").json()

    assert len(after) == initial_len + 1