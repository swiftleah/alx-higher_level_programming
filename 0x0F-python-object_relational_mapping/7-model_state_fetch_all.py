#!/usr/bin/python3
""" lists all State objects from database hbtn_0e_6_usa
    using SQlAlchemy """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    myengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    newSession = sessionmaker(bind=myengine)
    session = newSession()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
