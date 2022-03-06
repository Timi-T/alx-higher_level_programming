#!/usr/bin/python3

"""
modlue to access a database using the MySQLdb module
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    mydb = MySQLdb.connect(user=username, passwd=password, db=db_name)
    db_cursor = mydb.cursor()
    q = """SELECT * FROM states WHERE name REGEXP '^N' ORDER BY states.id"""
    db_cursor.execute(q)
    table = db_cursor.fetchall()

    for row in table:
        print(row)
