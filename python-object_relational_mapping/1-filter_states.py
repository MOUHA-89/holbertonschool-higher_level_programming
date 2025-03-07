#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get states starting
    # with 'N' and order them by state.id
    cursor.execute(
        "SELECT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all the results
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state[0])

    # Close the cursor and connection
    cursor.close()
    db.close()
