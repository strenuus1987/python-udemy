import sqlite3

def create_table():
    #Steps:
    #1. Connect to database
    connection = sqlite3.connect("my.db")
    #2. Create a cursor object
    cursor = connection.cursor()
    #3. Write an SQl query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #4. Commit changes
    connection.commit()
    #5. Close database connection
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    res = cursor.fetchall()
    connection.close()
    return res

def delete(item):
    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()

def update(item, price, quantity):
    connection = sqlite3.connect("my.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    connection.commit()
    connection.close()

create_table()
# insert('water glass', 5, 15)
# insert('coffee cup', 2, 30)
# delete('water glass');
#update('coffee cup', 5, 35.5)
print(view())
