#!/usr/bin/python3
"""Database Engine
   This is the db storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    """QLAlchemy will be your best friend!
        It’s time to change your storage engine and use SQLAlchemy
    """
    __engine = None
    __session = None

    def __init__(self):
        """"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if HBNB_DEV = 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """method must return a dictionary like file storage"""
        dict_query = {}
        if cls:
            query = self.__session.query(cls).all()
            key = cls.__name__ + '.'
            for iter in query:
                dict_query[key + iter.id] = iter
            return dict_query
        else:
            for allclass_iter in [State, City, User, Place, Review, Amenity]:
                query = self.__session.query(allclass_iter).all()
                key = allclass_iter.__name__ + '.'
                for iter in query:
                    dict_query[key + iter.id] = iter
            return dict_query

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            delete_obj = session.query(
                type(obj)).filter(
                type(
                    obj.id).like(
                    obj.id))
            session.delete(delete_obj)
            self.save()

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy) and
        create the current database session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))()

    def close(self):
        """ call method close session
        """
        self.__session.close()
