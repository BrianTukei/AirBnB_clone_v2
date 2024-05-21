#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import models


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), nullable=False, ForeignKey('place_id'))
    user_id = Column(String(60), nullable=False, ForeignKey('place_id'))
    text = Column(String(1024), nullable=False)
