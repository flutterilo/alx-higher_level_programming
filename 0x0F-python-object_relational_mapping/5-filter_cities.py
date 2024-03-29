#!/usr/bin/python3
'''
script that takes in the name of a state
as an argument and lists all cities of that state
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id \
                ORDER BY c.id ASC")
    cities = cur.fetchall()
    print(", ".join([city[1] for city in cities
          if city[2] == sys.argv[4]]))
