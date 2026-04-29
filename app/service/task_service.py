# ГЛАВНАЯ ИДЕЯ SERVICE -
# Аналогия - рабочий, который пишет/читает

# service = “мозг” -
# repo = делает
# service = решает

# импортируем repo — слой работы с базой
from app.repo import task_repo

# тип Session (передаём db дальше)
from sqlalchemy.orm import Session


def create_task(db: Session, title: str, description: str | None):
    # БИЗНЕС-ЛОГИКА:
    # проверяем, что title не пустой
    if not title:
        raise ValueError("Title is required")

    # вызываем repo для создания задачи
    task = task_repo.create_task(db, title, description)

    # возвращаем результат
    return task


def get_task(db: Session, task_id: int):
    # просто делегируем в repo
    return task_repo.get_task(db, task_id)


def get_tasks(db: Session):
    # можно добавить фильтры или логику позже
    return task_repo.get_tasks(db)


def delete_task(db: Session, task_id: int):
    # получаем задачу
    task = task_repo.get_task(db, task_id)

    # бизнес-логика: если нет задачи — ошибка
    if not task:
        raise ValueError("Task not found")

    # удаляем через repo
    return task_repo.delete_task(db, task_id)