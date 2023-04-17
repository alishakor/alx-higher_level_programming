#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
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
    Define the SQL query with a parameter and
    define the parameter value
    """
    state_name = sys.argv[4]

    query = "SELECT cities.name FROM cities INNER JOIN \
            states ON cities.state_id = states.id WHERE \
            states.name like BINARY %s ORDER BY cities.id"
    """
    Execute an SQL query to retrieve data
    """
    cursor_obj.execute(query, (state_name,))
    """
    Fetch all the rows returned by the query and
    loop through the rows and print the data
    """
    selected_rows = cursor_obj.fetchall()
    citynames = [row[0] for row in selected_rows]
    citylist = ', '.join(citynames)
    print(citylist)
    """
    close the cursor object
    """
    cursor_obj.close()
    """
    close the database connection
    """
    conn.close()
