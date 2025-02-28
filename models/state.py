#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base if getenv
            ('HBNB_TYPE_STORAGE') == 'db' else object):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

    @property
    def cities(self):
        """ getter for cities """
        from models import storage
        from models.city import City

        all_cities = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                all_cities.append(city)
        return all_cities
