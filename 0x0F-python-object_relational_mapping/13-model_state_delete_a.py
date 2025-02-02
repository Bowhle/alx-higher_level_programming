#!/usr/bin/python3
"""
Delete all State objects with a name containing
the letter a.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

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

    states = (session.query(State)
              .filter(State.name.ilike("%a%"))
              .all())
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
