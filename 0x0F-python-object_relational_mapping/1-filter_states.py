#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()

    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'
                 ORDER BY id ASC")
    states = curs.fetchall()

    for state in states:
        formated_state = "({}, '{}')".format(state[0], state[1])
        print(formated_state)
    curs.close()
    db.close()
