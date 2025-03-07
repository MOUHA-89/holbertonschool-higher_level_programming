#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL credentials from command-line arguments
    username = sys.argv[1]  # MySQL username
    password = sys.argv[2]  # MySQL password
    database = sys.argv[3]  # Database name

    # Establish connection to MySQL server
    db = MySQLdb.connect(
        host="localhost",  # Database server address (localhost)
        user=username,       # Username provided as argument
        passwd=password,     # Password provided as argument
        db=database          # Database name provided as argument
    )
    cursor = db.cursor()  # Create a cursor object to interact with the database

    # Execute SQL query to retrieve all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display all records
    for state in cursor.fetchall():
        print(state)
    
    # Close the cursor and database connection to free resources
    cursor.close()
    db.close()
