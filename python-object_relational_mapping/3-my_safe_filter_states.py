#!/usr/bin/python3
"""Displays the states whose name matches the argument, safe from injection.

The user input is passed to execute as a parameter, so MySQLdb escapes it
instead of treating it as part of the SQL text.
"""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
