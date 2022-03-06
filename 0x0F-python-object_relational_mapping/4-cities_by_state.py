#!/usr/bin/python3
"""
module that lists all cities from a database
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    mydb = MySQLdb.connect(user=usr, passwd=pw, db=db_name)
    db_cursor = mydb.cursor()
    txt1 = "SELECT cities.id, cities.name, states.name FROM cities"
    txt2 = "LEFT JOIN states ON cities.state_id=states.id ORDER BY cities.id"
    sql_txt = txt1 + ' ' + txt2
    db_cursor = mydb.cursor()
    db_cursor.execute(sql_txt)

    cities = db_cursor.fetchall()

    for city in cities:
        print(city)
