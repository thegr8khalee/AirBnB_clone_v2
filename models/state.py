#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base_model import Base
from os import getenv
import models
from models.city import City
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities():
            """_summary_
            """
            cityList = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:  # noqa: F821
                    cityList.append(city)
            return cityList
            