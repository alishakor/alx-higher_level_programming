#!/usr/bin/python3

"""
a script that prints the first State object from the database hbtn_0e_0_usa
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
    write query to be executed
    """
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    """
    close the session
    """
    session.close()
