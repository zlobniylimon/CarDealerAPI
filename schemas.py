from typing import List, Optional
from pydantic import BaseModel

class CarBase(BaseModel):
    model: str
    price: int
    dealer_id: int

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True
        
class CarDealerBase(BaseModel):
    name: str

class CarDealerCreate(CarDealerBase):
    pass

class CarDealerUpdate(CarDealerBase):
    pass

class CarDealer(CarDealerBase):
    id: int
    cars: List[Car] = []

    class Config:
        orm_mode = True
