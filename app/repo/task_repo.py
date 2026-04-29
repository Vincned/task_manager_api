# Аналогия - рабочий, который пишет/читает.
# 👉 Это слой, который:
# * говорит с базой данных
# * делает CRUD (create/read/update/delete)
# * НЕ содержит бизнес-логики
# * НЕ знает про FastAPI

# Главная идея REPO
# repo = ТОЛЬКО работа с базой
# никакой логики
# никакого FastAPI

# Объяснение используемых модулей внутри функций
# 🔹 db: Session
# 👉 это “подключение к базе”
#
# 🔹 db.add()
# 👉 подготовить запись
#
# 🔹 db.commit()
# 👉 сохранить в базу
#
# 🔹 db.refresh()
# 👉 получить обновлённые данные (например id)
#
# 🔹 query()
# 👉 “SQL в Python стиле”

# импортируем модель Task (таблица)
from app.models.task import Task

# импортируем SQLAlchemy Session (тип для db)
from sqlalchemy.orm import Session

def create_task(db: Session, title: str, description: str | None):
    # создаём объект таблицы Task
    task = Task(
        title=title,              # название задачи
        description=description   # описание задачи
    )

    # добавляем в сессию (пока не в базу)
    db.add(task)

    # сохраняем в базу
    db.commit()

    # обновляем объект (чтобы получить id)
    db.refresh(task)

    # возвращаем созданную задачу
    return task

def get_task(db: Session, task_id: int):
    # ищем одну задачу по id
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session):
    # возвращаем все задачи
    return db.query(Task).all()

def delete_task(db: Session, task_id: int):
    # ищем задачу
    task = db.query(Task).filter(Task.id == task_id).first()

    # если не нашли — ничего не делаем
    if not task:
        return None

    # удаляем из базы
    db.delete(task)

    # сохраняем изменения
    db.commit()

    # возвращаем удалённую задачу
    return task