#!/usr/bin/python3
"""Script lists all state objects from hbtn_0e_6_usa db."""

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost/{}"\
                           .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    session = sessionmaker(binddddd=engine)
    results = session.query(State).order_by(State.id)
    for state in results:
        print("{state.id}: {state.name}")
