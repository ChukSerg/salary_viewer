from fastapi import APIRouter

from app.api.endpoints import salary_router, user_router

main_router = APIRouter()
main_router.include_router(
    salary_router, prefix='/salary', tags=['Salary']
)
main_router.include_router(user_router)
