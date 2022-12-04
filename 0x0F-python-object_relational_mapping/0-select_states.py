#!/usr/bin/python3
"""
List all state from db
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    pter = db.cursor()
    pter.execute("SELECT * FROM states;")
    states = pter.fetchall()

    for state in states:
        print(state)