#!/usr/bin/python3
"""
module to get state names from states table
"""

import sys
from model_state import State, Base
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

    states = session.query(State).order_by(State.id)

    for state in states:
        print(state.id, ': ' + state.name)
