# Цель этого слоя - что приходит от пользователя и что мы возвращаем пользователю
# Цель файла - обмен данными через API

# Pydantic используется для валидации данных (проверка входящих/исходящих данных)
from pydantic import BaseModel


# 🔹 Схема для создания задачи (что приходит от клиента)
class TaskCreate(BaseModel):
    # название задачи обязательно
    title: str

    # описание задачи не обязательно
    description: str | None = None


# 🔹 Схема для обновления задачи
class TaskUpdate(BaseModel):
    # можно обновить название (или не передать)
    title: str | None = None

    # можно обновить описание
    description: str | None = None

    # можно отметить выполненной
    done: bool | None = None


# 🔹 Схема ответа (что мы отдаём пользователю)
class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None
    done: bool

    # важно: позволяет превращать SQLAlchemy объект → Pydantic
    class Config:
        from_attributes = True # Это мост между SQLAlchemy и Pydantic
        #без него:
        # * ORM объект не превращается в JSON нормально
        # * FastAPI ломается или отдаёт пусто