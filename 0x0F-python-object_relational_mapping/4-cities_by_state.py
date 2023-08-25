#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name,\
                 states.name FROM cities JOIN states\
                 ON cities.state_id = states.id ORDER\
                 BY cities.id ASC""")

    [print(row) for row in curs.fetchall()]
