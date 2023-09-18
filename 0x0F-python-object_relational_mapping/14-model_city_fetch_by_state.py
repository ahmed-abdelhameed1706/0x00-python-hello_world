#!/usr/bin/python3
"""
Script that prints all City objects
from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        arg1, arg2, arg3))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_and_states = session.query(City, State).join(
                        State).order_by(City.id).all()

    for city, state in cities_and_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
