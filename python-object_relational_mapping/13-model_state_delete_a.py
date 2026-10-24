#!/usr/bin/python3
"""Deletes all State objects whose name contains the letter a."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False)
    session.commit()
    session.close()
