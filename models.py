from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class CarDealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    cars = relationship("Car", back_populates="dealer")

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model = Column(String)
    price = Column(Integer)
    dealer_id = Column(Integer, ForeignKey("dealers.id"))

    dealer = relationship("CarDealer", back_populates="cars")