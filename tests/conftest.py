# настраивает тестовую среду ОДИН РАЗ для всех тестов

# 👉 сюда выносят:
# * фикстуры
# * подготовку БД
# * подмену зависимостей
# * TestClient

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.database import Base, engine, SessionLocal, get_db


# создаём таблицы перед тестами
Base.metadata.create_all(bind=engine)

# override DB dependency
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# подмена на тестовую базу, вместо реальной
app.dependency_overrides[get_db] = override_get_db

# test client
# фейковый браузер, позволяет работать без запуска сервера
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c