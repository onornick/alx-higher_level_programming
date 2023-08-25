#!/usr/bin/python3

""" takes in an argument
    and displays all values
    in the states table of
    hbtn_0e_0_usa where name matches the argument
     Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """checks if the file is being currently executed"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT id, name FROM states
                 WHERE name LIKE BINARY %(name)s
                 ORDER BY states.id ASC""", {'name': sys.argv[4]})
    rows = curs.fetchall()
    for row in rows:
        print(row)
