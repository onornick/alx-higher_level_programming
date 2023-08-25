#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
curs = db.cursor()
curs.execute("""
             SELECT cities.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name LIKE BINARY %(name)s
             ORDER BY cities.id""", {'name': sys.argv[4]})

rows = curs.fetchall()
names = ', '.join(row[0] for row in rows)
print(names)
