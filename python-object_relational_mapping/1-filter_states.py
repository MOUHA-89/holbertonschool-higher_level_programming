#!/usr/bin/python3
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

    cursor = db.cursor

    cursor = cursor.execute("SELECT * FROM states WHERE "
                            "name LIKE 'N%' BY ORDER id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
