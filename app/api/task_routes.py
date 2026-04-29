# создаём роутер (группа endpoints)
from fastapi import APIRouter, Depends, HTTPException

# импортируем сессию БД
from sqlalchemy.orm import Session

# импортируем функцию для получения db
from app.db.database import get_db

# импортируем схемы (контракты API)
from app.schemas.task import TaskCreate, TaskOut

# импортируем service слой (логика)
from app.service import task_service

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_task(
    task: TaskCreate,              # данные от клиента (валидируются через schema)
    db: Session = Depends(get_db) # получаем db через dependency injection
):
    # вызываем service (логика)
    new_task = task_service.create_task(
        db,
        task.title,
        task.description
    )

    # возвращаем результат (FastAPI сам превратит в JSON)
    return new_task


@router.get("/tasks", response_model=list[TaskOut])
def get_tasks(
    db: Session = Depends(get_db)  # получаем db
):
    # вызываем service
    return task_service.get_tasks(db)


@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete("/tasks/{task_id}", response_model=TaskOut)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    # вызываем service
    return task_service.delete_task(db, task_id)
