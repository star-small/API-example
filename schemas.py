from typing import List, Optional
from pydantic import BaseModel
import datetime


class Customer(BaseModel):
    title: str

    class Config:
        orm_mode = True


class Boss(BaseModel):
    fullname: str

    class Config:
        orm_mode = True


class Worker(BaseModel):
    id: int
    fullname: str
    customer_name: str
    boss_name: str
    date: datetime.date
    salary: int

    class Config:
        orm_mode = True
