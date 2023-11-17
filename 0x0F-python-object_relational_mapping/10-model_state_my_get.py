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

    state_match = session.query(State)\
        .filter(State.name == sys.argv[4]).first()

    if state_match:
        print(state_match.id)
    else:
        print("Not found")

    session.close()
