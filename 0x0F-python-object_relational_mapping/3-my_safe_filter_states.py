#!/usr/bin/python3
"""
script that takes in an arg and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306,
                         host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * FROM states")
    query_row = cur.fetchall()
    for row in query_row:
        if row[1] == arg:
            print(row)
