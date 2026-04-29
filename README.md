## Description
A simple Task Manager REST API built with FastAPI.
It allows creating, reading, updating and deleting tasks.
The project uses layered architecture (routes, services, models).

## Features
- Create task
- Get all tasks
- Get task by ID
- Delete task
- PostgreSQL/SQLite support
- Pytest tests with isolated DB

## Tech Stack
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite (test DB)
- Pytest

## Project Structure
app/
  api/
  service/
  models/
  schemas/
  db/

tests/

## How to run
### Install dependencies
pip install -r requirements.txt

### Run server
uvicorn app.main:app --reload

## How to test
pytest