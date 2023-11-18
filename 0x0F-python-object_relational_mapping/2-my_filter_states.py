#!/usr/bin/python3
"""Script to perform sql query."""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(args[1], passwd=args[2], db=args[3])
    exe = db.cursor()
    exe.execute(f"SELECT * FROM `states` WHERE BINARY `name` = {args[4]}")

    for state in exe.fetchall():
        print(state)

    exe.close()
