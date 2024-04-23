import sqlite3

def main():
    # Connect to the db
    conn = sqlite3.connect('company.db')

    # Get a cursor
    cur = conn.cursor()

    # Add the customer table
    cur.execute('''CREATE TABLE Customers (CustomerID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Email TEXT)''')

    # Add the employee table
    cur.execute('''CREATE TABLE Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Position TEXT)''')

    # Commit the changes
    conn.commit()

    # Close the connecyion
    conn.close()

# Execute main
main()
