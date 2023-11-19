#!/usr/bin/python3
"""Defines a State model from hbtn_0e_6_usa db.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class City(Base):
    """A city model for creatig city objects for
    MySQL database.

    id (sqlalchemy.Integer): City id in the table.
    name (sqlalchemy.String): City name in the table.
    __tablename__ (str): Table name to store cities.

    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    __tablename__ = "cities"
