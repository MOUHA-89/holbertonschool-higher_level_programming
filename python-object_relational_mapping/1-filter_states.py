#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments passed to the script
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query to find all states starting with 'N' ordered by state id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results in the desired format
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()
