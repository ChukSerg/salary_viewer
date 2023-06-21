from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud.salary import salary_crud
from app.schemas.salary import SalaryCreate, SalaryDB

router = APIRouter()


@router.post('/',
             response_model=SalaryDB)
async def create_new_salary(
    salary: SalaryCreate,
    session: AsyncSession = Depends(get_async_session)
):
    # salary_id = await get_salary_id(current_user)
    # if salary_id is not None:
    #     raise HTTPException(
    #         status_code=422,
    #         detail='Зарплата пользователя с таким именем уже существует!',
    #     )

    new_salary = await salary_crud.create (salary, session)
    return new_salary


@router.get(
    '/',
    response_model=list[SalaryDB]
)
async def get_all_salaries(
    session: AsyncSession = Depends(get_async_session)
):
    all_salaries = await salary_crud.get_multi(session)
    return all_salaries
