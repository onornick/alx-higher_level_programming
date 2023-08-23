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

    curs.execute("SELECT * FROM state WHERE name LIKE 'N%' ORDER BY id")
    rows = curs.fetchall()

    for row in rows:
        print(row)

    curr.close()
    db.close()
