#!/usr/bin/python3
"""
prints first state object from the database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


user = sys.argv[1]
pwd = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    eng_txt = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)
    engine = create_engine(eng_txt, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).filter(State.id == 1).first()
    print("{}: {}".format(first_state.id, first_state.name))
