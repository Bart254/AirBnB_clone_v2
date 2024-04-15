#!/usr/bin/python3
""" DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base


class DBStorage:
    """ DataBase Storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialiazes instances of DBStorage class
        """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Returns all objects depending on cls, if class is none,
        queries all objects
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        obj_dict = {}
        classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Review': Review, 'Place': Place,
                   }
        if cls:
            if cls in classes.values() or cls in classes.keys():
                if cls in classes.keys():
                    cls = classes[cls]
                for obj in self.__session.query(cls).all():
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict.update({key: obj})
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls).all():
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict.update({key: obj})
        return obj_dict

    def new(self, obj=None):
        """ Adds object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database object obj
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables from the database and also creates current
        database session
        """
        from models.city import City
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def close(self):
        self.__session.close()
