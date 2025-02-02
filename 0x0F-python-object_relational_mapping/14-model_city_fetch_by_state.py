#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(City, State)
               .filter(City.state_id == State.id)
               .order_by(City.id))

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
