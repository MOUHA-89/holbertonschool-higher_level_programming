#!/usr/bin/python3
""""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.arg[1]
    password = sys.arg[2]
    database = sys.arg[3]

db = MySQLdb.connect(host="localhost",
                     user=username,
                     passwd=password,
                     db=database)

cursor = db.cursor()

cursor.execute("SELECT name FROM states WHERE name Like 'N%' ORDER BY id ASC;")

for state in cursor.fetchall():
    print(state)

cursor.close()
db.close()
