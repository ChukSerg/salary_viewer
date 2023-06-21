from datetime import datetime

from pydantic import BaseModel


class SalaryCreate(BaseModel):
    salary: int
    date_of_raising: datetime


class SalaryDB(SalaryCreate):
    id: int

    class Config:
        orm_mode = True
