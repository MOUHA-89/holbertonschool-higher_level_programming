#!/usr/bin/python3
""""
lists all states from the database hbtn_0e_0_usa"
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.arg[1]
    password = sys.arg[2]
    database = sys.arg[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

        cursor.close()
        db.close()
