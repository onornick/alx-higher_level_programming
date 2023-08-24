#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    state_name = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM states
                      WHERE name LIKE BINARY '{}'
                      ORDER BY states.id ASC""".format(state_name))

    [print(state) for state in db_cursor.fetchall()]
