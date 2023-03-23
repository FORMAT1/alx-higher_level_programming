#!/usr/bin/python3
"""
    A script that prints all City objects from the database hbtn_0e_6_usa
    Username, password and dbname wil be passed as arguments to the script.
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
i

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], sys.argv[3]),
                           
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # extract all cities in a state
    cities = session.query(State, City).join(state)

    # print all states

    for city, state in cities.all():
        print("{}: ({}) {}".format(State.name, City.id, City.name))

    session.commit()
    session.close()
