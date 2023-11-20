#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' \
   from hbtn_0e_6_usa db.
"""

import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)
    for state in result:
        if "a" in state.name:
            session.delete(state)
    session.commit()
    session.close()
