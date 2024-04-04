#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
from os import getenv

if getenv(HBNB_TYPE_STORAGE) == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage() 
=======
from models.engine.file_storage import FileStorage
#from models.engine.db_storage import DBStorage
from os import getenv
#from models.engine.file-storage import FileStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
>>>>>>> 10fd128bcff5b91b19bb395712cc208dc84559d3
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
