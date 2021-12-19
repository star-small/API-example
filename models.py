import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from db import Base


class Customer(Base):
    __tablename__ = "customers"
    title = Column(String, index=True, primary_key=True, autoincrement=False)
    workers = relationship("Worker", back_populates="owner")


class Boss(Base):
    __tablename__ = "boss"
    fullname = Column(String, autoincrement=False, primary_key=True)
    workers = relationship("Worker")


class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    boss_name = Column(String, ForeignKey("boss.fullname"))
    customer_name = Column("Должность", Integer, ForeignKey("customers.title"))
    date = Column(Date, default=datetime.datetime.utcnow)
    salary = Column(Integer)
    owner = relationship("Customer", back_populates="workers")
