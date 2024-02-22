#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),  ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            place_reviews = []
            for obj in storage.all(Review).values():
                if obj.place_id == self.id:
                    place_reviews.update(obj)
            return place_reviews

        @property
        def amenities(self):
            from models.amenity import Amenity
            all_amenities = []
            for obj in storage.all(Amenity).values():
                if obj.id in self.amenity_ids:
                    all_amenities.append(obj)
            return all_amenities

        @amenities.setter
        def amenities(self, amenity):
            from models.amenity import Amenity
            if type(amenity) is Amenity:
                self.amenity_ids.append(amenity.id)
