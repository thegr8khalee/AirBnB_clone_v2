#!/usr/bin/python3
"""_summary_"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """_summary_"""

    __engine = None
    __session = None

    def __init__(self):
        """_summary_"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__engine.query(cls)
        elif cls is None:
            objects = self.__engine.query(State).all()
            objects.extend(self.__engine.query(User). all())
            objects.extend(self.__engine.query(City). all())
            objects.extend(self.__engine.query(Amenity). all())
            objects.extend(self.__engine.query(Place). all())
            objects.extend(self.__engine.query(Review). all())
        else:
            return {"{}.{}".format(type(x).__name__, x.id): x for x in objects}
        
    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        self.__session.add(obj)
        
    def save(self):
        """_summary_
        """
        self.__session.commit()
        
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            
    def reload(self):
        """_summary_
        """
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
