from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Check connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dealers/", response_model=schemas.CarDealer)
def create_new_dealer(dealer: schemas.CarDealerCreate, db: Session = Depends(get_db)):
    db_dealer = crud.read_dealer_by_name(db=db, dealer_name=dealer.name)
    if db_dealer:
        raise HTTPException(status_code=409, detail="Dealer's name is already used'")
    db_dealer = crud.create_dealer(db=db, dealer=dealer)
    return db_dealer

@app.get("/dealers/", response_model=List[schemas.CarDealer])
def read_all_dealers(db: Session = Depends(get_db)):
    db_dealers = crud.read_dealers(db=db)
    return db_dealers

@app.get("/dealers/{dealer_id}", response_model=schemas.CarDealer)
def read_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.read_dealer(db=db, dealer_id=dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return db_dealer

@app.put("/dealers/{dealer_id}", response_model=schemas.CarDealer)
def update_dealer(dealer_id: int, dealer: schemas.CarDealerUpdate, db: Session = Depends(get_db)):
    db_dealer = crud.read_dealer(db=db, dealer_id=dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    db_dealer = crud.update_dealer(db=db, dealer_id=dealer_id, dealer=dealer)
    return db_dealer

@app.delete("/dealers/{dealer_id}")
def delete_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.read_dealer(db=db, dealer_id=dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    crud.delete_dealer(db=db, dealer_id=dealer_id)
    return Response(status_code=204)

@app.post("/cars/", response_model=schemas.Car)
def create_new_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.create_car(db=db, car=car)
    return db_car

@app.get("/cars/", response_model=List[schemas.Car])
def read_all_cars(db: Session = Depends(get_db)):
    db_cars = crud.read_cars(db=db)
    return db_cars

@app.get("/cars/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.read_car(db=db, car_id=car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db_car = crud.read_car(db=db, car_id=car_id)
    return db_car

@app.put("/cars/{car_id}", response_model=schemas.Car)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    db_car = crud.read_car(db=db, car_id=car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db_car = crud.update_car(db=db, car_id=car_id, car=car)
    return db_car

@app.delete("/cars/{car_id}")
def delete_car(car_id:int, db: Session = Depends(get_db)):
    db_car = crud.read_car(db=db, car_id=car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    crud.delete_car(db=db, car_id=car_id)
    return Response(status_code=204)