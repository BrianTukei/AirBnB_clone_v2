#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('place.id'),
                             nullable=False),
                      Column('amenity_id', String(60), ForeignKey
                             ('amenities.id'), nullable=False))


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, default=0,
                     Foreignkey('cities.id'))
    user_id = Column(String(60), nullable=False, default=0,
                     Foreignkey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=0)
    longitude = Column(Float, nullable=True, default=0)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref="place_amenities")

    @property
    def reviews(self):
        """Review getter - return list of filtered reviews."""
        reviews_instances = []
        reviews_dict = models.storage.all('Review')
        for key, value in reviews_dict.items():
            if self.id == value.place_id:
                reviews_instances.append(value)
        return reviews_instances

    @property
    def amenities(self):
        """Review getter - return list of amenity instances"""
        amenities_instances = []
        amenities_dict = models.storage.all('Amenity')
        for key, value in amenities_dict.items():
            for iter_id in self.amenity_ids:
                if value.id == iter_id:
                    amenities_instances.append(value)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """Setter for amenity list
           Setter attribute amenities that handles append method
           for adding an Amenity.id
           or isinstance(obj, Amenity):
        """
        if obj.__name__ == Amenity:
            self.ammenity_ids.append(obj.id)
