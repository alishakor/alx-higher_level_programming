#!/usr/bin/python3

"""
a script that changes the name of a State object from the
database hbtn_0e_6_usa
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
    Write Query for the database and update the state
    """
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    """
    Close the session
    """
    session.close()
