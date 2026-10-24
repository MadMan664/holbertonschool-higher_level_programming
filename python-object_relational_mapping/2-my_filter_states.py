#!/usr/bin/python3
"""Displays the states whose name matches the argument, using str.format.

The query is built by formatting the user input into the SQL text, so it
is open to SQL injection. The safe version is in 3-my_safe_filter_states.py.
"""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' "
                "ORDER BY id ASC".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
