from sqlalchemy import Column, DateTime, Integer, ForeignKey

from app.core.db import Base


class Salary(Base):
    salary = Column(Integer)
    date_of_raising = Column(DateTime)
    # user = Column(Integer, ForeignKey)
