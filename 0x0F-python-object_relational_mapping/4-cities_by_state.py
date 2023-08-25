#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

    Your script should take 3 arguments: user, passwd and db
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Write a script that lists all cities from the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name,\
                 states.name FROM cities JOIN states\
                 ON cities.state_id = states.id ORDER\
                 BY cities.id ASC""")

    [print(row) for row in curs.fetchall()]
