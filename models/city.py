#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
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