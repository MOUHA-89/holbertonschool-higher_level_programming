#!/usr/bin/python3
""""
"takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."
"""
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
        st=state,
    )

    cursor = db.cursor()

    query = "SELECT *FROM states WHERE name like '{}'.format(state) ORDER BY id ASC"

    cursor.execute(query, (state,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close()
