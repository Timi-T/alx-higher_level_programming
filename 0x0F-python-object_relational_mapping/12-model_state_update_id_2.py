#!/usr/bin/python3


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


user = sys.argv[1]
pwd = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    eng_txt = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)
    engine = create_engine(eng_txt, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).filter(State.id == 2).first()
    st.name = 'New Mexico'
    session.commit()
