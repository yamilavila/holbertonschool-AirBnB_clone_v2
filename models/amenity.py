#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from os import getenv


class Amenity(BaseModel, Base):
    """class amenity attributes """
    __tablename__ = "amenities"
    name = Column(String(128),
                  nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship(
                "Place",
                secondary="place_amenity",
                viewonly=False,
                back_populates="amenities")
