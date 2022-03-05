#!/usr/bin/python3


import MySQLdb
import sys


usr = sys.argv[1]
pw = sys.argv[2]
db_name = sys.argv[3]
state_name = "'" + sys.argv[4] + "'"

mydb = MySQLdb.connect(user=usr, passwd=pw, db=db_name)
db_cursor = mydb.cursor()
txt1 = "SELECT name FROM cities "
txt2 = "WHERE state_id = "
txt3 = "(SELECT id FROM states "
txt4 = "WHERE name = {}) ".format(state_name)
txt5 = "ORDER BY cities.state_id"
sql_txt = txt1 + txt2 + txt3 + txt4

db_cursor.execute(sql_txt)
cities = db_cursor.fetchall()

cty_str = ''
i = 1
for city in cities:
    if (i != len(cities)):
        cty_str += city[0] + ', '
    else:
        cty_str += city[0]
    i += 1
print(cty_str)
