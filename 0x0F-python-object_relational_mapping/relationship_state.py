#!/usr/bin/python3
"""Defines a State model from hbtn_0e_6_usa db.
"""

from relationship_city import City, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class City(Base):
    """A state model for creatig state objects for
    MySQL database.

    id (sqlalchemy.Integer): State id in State table.
    name (sqlalchemy.String): State name in State table.
    cities: State-City relationship.
    __tablename__ (str): Table name to store state.

    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = "sates"
