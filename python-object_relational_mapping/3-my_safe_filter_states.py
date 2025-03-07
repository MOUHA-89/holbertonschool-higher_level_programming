#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.arg[1]
    password = sys.arg[2]
    database = sys.arg[3]
    state = sys.arg[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        st=state
    )

    cursor = db.cursor()

    cursor.execute("SELECT *FROM state WHERE name LIKE %s ORDER BY id ASC, (match, )")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close()
