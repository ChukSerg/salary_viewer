from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_user_duplicate, check_user_exists, check_salary_exists
)
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.base import CRUDBase
from app.crud.salary import salary_crud
from app.models import User
from app.schemas.salary import SalaryCreate, SalaryDB, SalaryMyDB
from app.schemas.user import UserRead

router = APIRouter()


@router.post('/',
             response_model=SalaryDB,
             dependencies=[Depends(current_superuser)],
             )
async def create_new_salary(
    salary: SalaryCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_user_duplicate(salary.user, session)
    await check_user_exists(salary.user, session)

    new_salary = await salary_crud.create(salary, session)
    return new_salary


@router.get(
    '/',
    response_model=list[SalaryDB],
    dependencies=[Depends(current_superuser)],
)
async def get_all_salaries(
    session: AsyncSession = Depends(get_async_session),
):
    all_salaries = await salary_crud.get_multi(session)
    return all_salaries


@router.delete(
    '/{user_id}',
    response_model=SalaryDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_salary(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salary = await check_salary_exists(
        user_id, session
    )
    salary = await salary_crud.remove(
        salary, session
    )
    return salary


@router.get(
    '/users',
    response_model=list[UserRead],
    dependencies=[Depends(current_superuser)],
)
async def get_all_users(
    session: AsyncSession = Depends(get_async_session),
):
    users_crud = CRUDBase(User)
    all_users = await users_crud.get_multi(session)
    return all_users


@router.get(
    '/my', response_model=SalaryMyDB
)
async def get_my_salary(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    salary = await check_salary_exists(
        user_id=user.id, session=session
    )
    salary = await salary_crud.get(
        salary.id, session=session
    )
    return salary
