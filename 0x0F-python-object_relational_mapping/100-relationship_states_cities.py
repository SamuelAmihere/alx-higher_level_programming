#!/usr/bin/python3
"""Creates the State 'California' with the City \
'San Francisco' in hbtn_0e_6_usa db.
"""

import sys
from model_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(args[1],
                                                      args[2], args[3])
    engine = create_engine(url=url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = "San Francisco"
    state = "California"
    session.add(City(name=city, state=State(name=state)))
    session.commit()
