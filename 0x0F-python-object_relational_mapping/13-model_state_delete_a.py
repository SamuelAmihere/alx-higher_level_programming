#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' \
    from hbtn_0e_6_usa db.
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)
    for state in result:
        if "a" in state.name:
            session.delete(state)
    session.commit()
