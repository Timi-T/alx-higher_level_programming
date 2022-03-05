#!/usr/bin/python3


import sys
from model_city import City
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

    ct = session.query(City).filter(State.id.in_(Childtable.state.id)).all().order_by(City.id)
    for city in ct:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
