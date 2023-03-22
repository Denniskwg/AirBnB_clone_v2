#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel,base
from sqlalchemy import Column,String,Integer,ForeignKey

class City(BaseModel, base):
    """ The city class, contains state ID and name """
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(String(60),ForeignKey("states.id"),nullable = False)
    name = Column(String(128),nullable = False )

    def __init__(self, **kwargs):
        from models import storage
        BaseModel.__init__(self)
        self.__dict__.update(kwargs)
        storage.new(self)

    __tablename__ = "cities"
