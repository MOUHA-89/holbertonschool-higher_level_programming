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
                     user="your_username",
                     passwd="your_password",
                     db="hbtn_0e_0_usa")

cursor = db.cursor()

query = "SELECT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

cursor.execute(query)

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()
