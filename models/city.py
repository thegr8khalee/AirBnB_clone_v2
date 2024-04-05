#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nulable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False, )
    
    states = relationship('states', back_populates='cities')
    states = relationship('cities', back_populates='states')
    places = relationship("Places", backref="cities", cascade="delete")
=======
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
