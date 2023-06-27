from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.salary import salary_crud
from app.models import Salary


async def check_user_duplicate(
        user: int,
        session: AsyncSession,
) -> None:
    salary_id = await salary_crud.get_by_user(user, session)
    if salary_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Зарплата пользователя с таким именем уже существует!',
        )


async def check_user_exists(
        user_id: int,
        session: AsyncSession,
) -> None:
    user = await salary_crud.get_user(user_id, session)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='Пользователя с таким именем не существует!',
        )


async def check_salary_exists(
        user_id: int,
        session: AsyncSession,
) -> Salary:
    salary = await salary_crud.get_by_user(user_id, session)
    if salary is None:
        raise HTTPException(
            status_code=404,
            detail='Зарплата не введена, обратитесь к администратору!'
        )
    return salary
