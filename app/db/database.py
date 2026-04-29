# импортируем SQLAlchemy инструменты для работы с базой данных
from sqlalchemy import create_engine

# sessionmaker создаёт "фабрику сессий" (подключений к БД)
from sqlalchemy.orm import sessionmaker

# declarative_base — базовый класс для всех моделей (таблиц)
from sqlalchemy.orm import declarative_base


# URL подключения к базе данных
DATABASE_URL = "sqlite:///./test.db"

# Как кабель к базе данных
# создаём "движок" — это объект, который реально общается с БД
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # нужно только для SQLite
)

# Создатель подключений
# создаём фабрику сессий (каждый вызов = новая сессия)
SessionLocal = sessionmaker(
    autocommit=False,  # не сохранять автоматически
    autoflush=False,   # не отправлять изменения сразу
    bind=engine        # привязка к engine (к базе)
)

# Основа для таблиц
# базовый класс для всех моделей (таблиц)
Base = declarative_base()

# Выдает подключение и закрывает его
# функция, которая будет давать нам сессию к БД
def get_db():
    # создаём новую сессию
    db = SessionLocal()

    try:
        # отдаём её наружу (в FastAPI route)
        yield db
    finally:
        # после запроса всегда закрываем соединение
        db.close()