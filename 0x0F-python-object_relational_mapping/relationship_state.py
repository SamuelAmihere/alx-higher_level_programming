#!/usr/bin/python3
"""Defines a State model from hbtn_0e_6_usa db.
"""

from relationship_city import City, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """A state model for creatig state objects for
    MySQL database.

    id (sqlalchemy.Integer): State id in State table.
    name (sqlalchemy.String): State name in State table.
    cities: State-City relationship.
    __tablename__ (str): Table name to store state.

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
