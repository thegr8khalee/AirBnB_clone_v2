#!/usr/bin/python3
"""_summary_"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class DBStorage:
    """New engine"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        """drop all tables if the environment variable HBNB_ENV is equal to test"""
        if getenv("HBNH_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(User)).all()
            objects.extend(self.__session.query(City)).all()
            objects.extend(self.__session.query(Amenity)).all()
            objects.extend(self.__session.query(Place)).all()
            objects.extend(self.__session.query(Review)).all()
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objects = self.__session.query(cls)
        for object in objects:
            return "<{}>.<{}>".format(type(object).__name__, object.id)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sss = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sss)
        
        """self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)"""
    
    """def all(self, cls=None):
        
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
        
        self.__session.add(obj)
        
    def save(self):
        
        self.__session.commit()
        
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            
    def reload(self):
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()"""

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
        