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
    state_name = "'" + state_name + "'"

    mydb = MySQLdb.connect(user=username, passwd=password, db=db_name)
    db_cursor = mydb.cursor()
    txt1 = "SELECT * FROM states WHERE "
    txt2 = "name = {} ORDER BY states.id".format(state_name)
    db_cursor.execute(txt1 + txt2)
    states = db_cursor.fetchall()

    for each_state in states:
        print(each_state)
