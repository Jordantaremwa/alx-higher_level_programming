#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to interact with MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name),
                           pool_pre_ping=True)

    # Create configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for states containing letter 'a' sorted by state id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

