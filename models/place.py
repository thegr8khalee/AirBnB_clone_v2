#!/usr/bin/python3
"""Place Module for HBNB project"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.Amenity import Amenity
from models.Review import Review
from models.base_model import Base
import models

alchemy_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    reviews = relationship("Reviews", backref="places", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":

        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """_summary_"""
            am_list = []
            for i in list(models.storage.all(Amenity).values()):
                if i.id in self.amenity_ids:
                    am_list.append(i)
                return

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
