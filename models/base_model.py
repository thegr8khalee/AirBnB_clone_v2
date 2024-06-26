#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
from sqlalchemy import String, Column, DateTime
=======
from sqlalchemy import Column, String, DateTime
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
import models


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

<<<<<<< HEAD
    id = Column(
        String(60), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
=======
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullaable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    """def __init__(self, *args, **kwargs):
        ""/"Instatntiates a new model""/"
        if not kwargs:
            #from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)"""
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3

    def __init__(self, *args, **kwargs):
        """_summary_"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
<<<<<<< HEAD
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
=======
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
<<<<<<< HEAD
=======
        #from models import storage

>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
<<<<<<< HEAD
        """_summary_"""
=======
        """_summary_
        """
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
        models.storage.delete(self)
