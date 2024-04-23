import sqlite3

def main():
    # Connect to the db
    conn = sqlite3.connect('inventory.db')

    # Get a cursor
    cur = conn.cursor()

    # Add the inventory to the table
    cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL, ItemName TEXT, Price REAL)''')

    # Commit the changes
    conn.commit()

    # Close the connecyion
    conn.close()

# Execute main
main()
