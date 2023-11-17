#!/usr/bin/python3
""" adds new state 'Louisiana' """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    myengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    newSession = sessionmaker(bind=myengine)
    session = newSession()

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()

    print(newState.id)

    session.close()
