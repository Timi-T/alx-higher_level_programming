#!/usr/bin/python3

"""
module to print all cities in a state
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = "'" + sys.argv[4] + "'"

    mydb = MySQLdb.connect(user=usr, passwd=pw, db=db_name)
    db_cursor = mydb.cursor()
    txt1 = "SELECT cities.id, cities.name, states.name "
    txt2 = "FROM cities LEFT JOIN states ON "
    txt3 = "cities.state_id = states.id "
    txt4 = "WHERE states.name = {} ".format(state_name)
    txt5 = "ORDER BY cities.id"
    sql_txt = txt1 + txt2 + txt3 + txt4

    db_cursor.execute(sql_txt)
    cities = db_cursor.fetchall()

    cty_str = ''
    i = 1
    for city in cities:
        if (i != len(cities)):
            cty_str += city[1] + ', '
        else:
            cty_str += city[1]
        i += 1
    print(cty_str)
