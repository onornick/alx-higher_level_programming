#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM states
                      WHERE name LIKE BINARY '{}'
                      ORDER BY states.id ASC""".format(sys.argv[4]))
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)

    db_cursor.close()
    db.close()
