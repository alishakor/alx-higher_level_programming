#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connect to the database
    """
    conn = MySQLdb.connect(
                user=sys.argv[1],
                host="localhost",
                port=3306,
                password=sys.argv[2],
                db=sys.argv[3])
    """
    Creates the cursor object to interact with database
    """
    cursor_obj = conn.cursor()
    """
    Define the SQL query with a parameter
    """
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC"

    """
    Execute an SQL query to retrieve data
    """
    cursor_obj.execute(query)
    """
    Fetch all the rows returned by the query and
    loop through the rows and print the data
    """
    selected_rows = cursor_obj.fetchall()
    for row in selected_rows:
        print(row)
    """
    close the cursor object
    """
    cursor_obj.close()
    """
    close the database connection
    """
    conn.close()
