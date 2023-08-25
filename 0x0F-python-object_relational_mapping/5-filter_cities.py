#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

    Your script should take 4 arguments: mysql username,
    mysql password, database name and state name (SQL injection
    free!)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    The results must be displayed as they are in the example below
    Your code should not be executed when imported

"""

import MySQLdb
import sys

if __name__ == "__main__":
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
