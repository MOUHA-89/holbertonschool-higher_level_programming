#!/usr/bin/python3
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
    print(state[0])

cursor.close()
db.close()
