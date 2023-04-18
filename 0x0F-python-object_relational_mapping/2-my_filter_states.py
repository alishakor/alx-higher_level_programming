#!/usr/bin/python3

"""
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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
    Execute an SQL query to retrieve data
    """
    cursor_obj.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(sys.argv[4]))
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
