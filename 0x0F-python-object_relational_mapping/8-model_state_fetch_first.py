#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        arg1, arg2, arg3), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
