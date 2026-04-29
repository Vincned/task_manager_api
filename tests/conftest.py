import pytest
from sqlalchemy.orm import Session

from app.main import app
from app.db.database import Base
from tests.database import engine, TestingSessionLocal

# создаём таблицы перед тестами
Base.metadata.create_all(bind=engine)


# override get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# подключаем override
from app.db.database import get_db
app.dependency_overrides[get_db] = override_get_db


# фикстура клиента
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)