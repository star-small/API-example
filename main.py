from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from db import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/getCustomersByBoss/{boss_name}", response_model=List[schemas.Worker])
def read_worker(boss_name: str, db: Session = Depends(get_db)):
    workers = crud.get_workers_by_boss(db, boss_name=boss_name)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


@app.get("/getCustomersByCustomer/{customer_name}", response_model=List[schemas.Worker])
def read_worker(customer_name: str, db: Session = Depends(get_db)):
    workers = crud.get_workers_by_customer(db, customer_name=customer_name)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


@app.get("/salaryEquals/{salary}", response_model=List[schemas.Worker])
def read_worker(salary: int, db: Session = Depends(get_db)):
    workers = crud.get_workers_by_salary_equals(db, salary=salary)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


@app.get("/salaryMore/{salary}", response_model=List[schemas.Worker])
def read_worker(salary: int, db: Session = Depends(get_db)):
    workers = crud.get_workers_by_salary_more(db, salary=salary)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


@app.get("/salaryLess/{salary}", response_model=List[schemas.Worker])
def read_worker(salary: int, db: Session = Depends(get_db)):
    workers = crud.get_worker_by_salary_less(db, salary=salary)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


@app.get("/workerName/{name}", response_model=List[schemas.Worker])
def read_worker(name: str, db: Session = Depends(get_db)):
    workers = crud.get_worker_by_name(db, name=name)
    if workers is None:
        raise HTTPException(status_code=404, detail="Workers not found")
    return workers


# Get all workers
@app.get("/workers", response_model=List[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    res = crud.show_tree(db)
    print(res)
    print(workers, 'q')
    return workers


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
