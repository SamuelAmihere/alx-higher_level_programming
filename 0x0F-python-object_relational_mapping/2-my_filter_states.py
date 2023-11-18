#!/usr/bin/python3
"""Script to perform sql query."""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    state = args[4]
    db = MySQLdb.connect(args[1], passwd=args[2], db=args[3])
    exe = db.cursor()
    exe.execute("SELECT * FROM `states` \
	WHERE BINARY `name` = {}".format(state))

    for state in exe.fetchall():
        print(state)

    exe.close()
