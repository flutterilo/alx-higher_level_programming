#!/usr/bin/python3
'''script that lists all states with a name starting with N'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY id ASC".format(sys.argv[4]))
    states = cur.fetchall()
    if states:
        for state in states:
            print(state)
