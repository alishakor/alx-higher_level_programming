#!/usr/bin/python3

"""
a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a new database engine
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """
    Create all tables defined in the models
    """
    Base.metadata.create_all(engine)

    """
    Create a new session to interact with engine
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    """
    write query to be executed and define the parameter value
    """
    state_name = sys.argv[4]

    states = session.query(State).filter(State.name.like(
        f'%{state_name}')).all()
    if states:
        for state in states:
            print(state.id)
    else:
        print("Not Found")
    """
    close the session
    """
    session.close()
