#!/usr/bin/python3
"""
module to prevent sql injection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    mydb = MySQLdb.connect(user=username, passwd=password, db=db_name)
    db_cursor = mydb.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY states.id",
            (state_name, ))
    states = db_cursor.fetchall()

    for each_state in states:
        print(each_state)
