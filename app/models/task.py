# Аналогия - Чертеж таблицы
# Этот файл это структура данных в БД
# Нет логики, только описание таблицы

# импортируем Base — это основа для всех таблиц
from app.db.database import Base

# SQLAlchemy инструменты для описания колонок
from sqlalchemy import Column, Integer, String, Boolean


# создаём таблицу Task в базе данных
class Task(Base):
    # имя таблицы в базе
    __tablename__ = "tasks"

    # id — уникальный идентификатор задачи
    id = Column(
        Integer,  # тип: число
        primary_key=True,  # это главный ключ
        index=True  # ускоряет поиск по id
    )

    # название задачи
    title = Column(
        String,  # текст
        index=True  # можно искать по нему
    )

    # описание задачи
    description = Column(
        String,  # текст
        nullable=True  # можно не указывать
    )

    # выполнена ли задача
    done = Column(
        Boolean,  # True / False
        default=False  # по умолчанию не выполнена
    )