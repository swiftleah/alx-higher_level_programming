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

    firstState = session.query(State).order_by(State.id).first()
    if firstState:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")

    session.close()
