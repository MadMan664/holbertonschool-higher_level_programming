#!/usr/bin/python3
"""Lists all State objects that contain the letter a, sorted by id."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.like("%a%"))
    for state in states.order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
