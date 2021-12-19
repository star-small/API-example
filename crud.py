from sqlalchemy import inspect
from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy.orm import join


def get_workers_by_boss(db: Session, boss_name):
    return db.query(models.Worker).filter(models.Worker.boss_name == boss_name).all()


def get_workers_by_customer(db: Session, customer_name):
    return db.query(models.Worker).filter(models.Worker.customer_name == customer_name).all()


def get_workers_by_salary_equals(db: Session, salary):
    return db.query(models.Worker).filter(models.Worker.salary == salary).all()


def get_workers_by_salary_more(db: Session, salary):
    return db.query(models.Worker).filter(models.Worker.salary >= salary).all()


def get_worker_by_salary_less(db: Session, salary):
    return  db.query(models.Worker).filter(models.Worker.salary <= salary).all()


def get_worker_by_name(db: Session, name):
    return db.query(models.Worker).filter(name == models.Worker.fullname).all()


def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()


def show_tree(db: Session):
    result = db.query(models.Worker).join(models.Boss).all()
    for worker in result:
        print(worker.fullname)
    return result
