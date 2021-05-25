from sqlalchemy.orm import Session
import models, schemas

def create_dealer(db: Session, dealer: schemas.CarDealerCreate):
    db_dealer = models.CarDealer(**dealer.dict())
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer

def update_dealer(db: Session, dealer_id: int, dealer: schemas.CarDealerUpdate):
    db_dealer = db.query(models.CarDealer).filter(models.CarDealer.id == dealer_id).first()
    db_dealer.update(**dealer.dict())
    db.commit()
    return db_dealer

def delete_dealer(db: Session, dealer_id: int):
    db.query(models.CarDealer).filter(models.CarDealer.id == dealer_id).delete()
    db.commit()
    return None

def read_dealer(db: Session, dealer_id: int):
    db_dealer = db.query(models.CarDealer).filter(models.CarDealer.id == dealer_id).first()
    return db_dealer

def read_dealer_by_name(db: Session, dealer_name: str):
    db_dealer = db.query(models.CarDealer).filter(models.CarDealer.name == dealer_name).first()
    return db_dealer

def read_dealers(db: Session):
    db_dealers = db.query(models.CarDealer).all()
    return db_dealers

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, car_id: int, car: schemas.CarUpdate):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    db_car.update(**car.dict())
    db.commit()
    return db_car

def delete_car(db: Session, car_id: int):
    db.query(models.Car).filter(models.Car.id == car_id).delete()
    db.commit()
    return None

def read_car(db: Session, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    return db_car

def read_cars(db: Session):
    db_cars = db.query(models.Car).all()
    return db_cars
    
