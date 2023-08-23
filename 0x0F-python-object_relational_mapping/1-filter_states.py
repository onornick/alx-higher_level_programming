#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])
    curs = db.cursor()

    curs.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

    curr.close()
    db.close()
