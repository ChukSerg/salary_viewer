from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Salary


class CRUDSalary(CRUDBase):

    async def get_by_user(
            self, user: int, session: AsyncSession,
    ):
        users_salary = await session.execute(
            select(Salary).where(
                Salary.user == user
            )
        )
        return users_salary.scalars().first()


salary_crud = CRUDSalary(Salary)
