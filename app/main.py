# импортируем FastAPI — основной класс приложения
from fastapi import FastAPI

# импортируем роутер с задачами
from app.api.task_routes import router as task_router

from app.core.exceptions import value_error_handler

# импортируем базу (для создания таблиц)
from app.db.database import Base, engine


# создаём приложение FastAPI
app = FastAPI()

# создаём все таблицы в базе (если их нет)
Base.metadata.create_all(bind=engine)

# подключаем маршруты задач
app.include_router(task_router)

# регистрируем обработчик
app.add_exception_handler(ValueError, value_error_handler)