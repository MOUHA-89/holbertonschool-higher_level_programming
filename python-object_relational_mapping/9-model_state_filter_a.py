#!/usr/bin/python3
""""
lists all State objects that contain the letter
a from the database hbtn_0e_6_usa"
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, dbname):

    engine = create_engine(f'mysql+mysqldb://{username}:'
                           '{password}@localhost:3306/{dbname}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./script.py "
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_states_with_a(username, password, dbname)
