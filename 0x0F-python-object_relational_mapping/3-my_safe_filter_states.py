#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE name LIKE BINARY '{}'
                 ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))

    [print(state) for state in curs.fetchall()]
