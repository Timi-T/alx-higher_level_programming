#!/usr/bin/python3

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
    db_cursor.execute("SET @state_name = {}".format(state_name))
    sql_txt = "SELECT * FROM states WHERE name=@state_name"
    db_cursor.execute(sql_txt)
    states = db_cursor.fetchall()

    for each_state in states:
        print(each_state)
