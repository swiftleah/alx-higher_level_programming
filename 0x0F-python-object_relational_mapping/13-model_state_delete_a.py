#!/usr/bin/python3
""" deletes all state objects containing the letter
    'a' from database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    myengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    newSession = sessionmaker(bind=myengine)
    session = newSession()

    to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in to_delete:
        session.delete(state)
    session.commit()

    session.close()
