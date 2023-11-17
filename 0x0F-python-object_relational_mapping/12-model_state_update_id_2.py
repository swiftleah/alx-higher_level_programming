#!/usr/bin/python3
""" Changes name of state where id = 2 to New Mexico """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    myengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    newSession = sessionmaker(bind=myengine)
    session = newSession()

    state_to_change = session.query(State).filter(State.id == 2).first()
    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()

    session.close()
