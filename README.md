# salary_viewer
FastAPI service to check current salary

установлена база данных на основе SQLite, для установки другой
необходимо вместо aiosqlite установить другой драйвер

Инициация Alembic:
в корневой дирректории выполнить команду:
alembic init --template async alembic - Создает папку Alembic, если есть, то не надо?

В файле .env добавить переменную DATABASE_URL=sqlite+aiosqlite:///./fastapi.db

все модели импортируем через core/base.py
alembic revision --autogenerate -m "First migration"
alembic upgrade head 
