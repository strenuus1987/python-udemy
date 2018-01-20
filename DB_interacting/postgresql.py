import psycopg2

def create_table():
    #Steps:
    #1. Connect to database
    connection = psycopg2.connect("dbname='store' user='postgres' password='postgres123' host='localhost' port='5432'")
    #2. Create a cursor object
    cursor = connection.cursor()
    #3. Write an SQl query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #4. Commit changes
    connection.commit()
    #5. Close database connection
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='store' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='store' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    res = cursor.fetchall()
    connection.close()
    return res

def delete(item):
    connection = psycopg2.connect("dbname='store' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    connection.commit()
    connection.close()

def update(item, price, quantity):
    connection = psycopg2.connect("dbname='store' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()
    connection.close()

create_table()
# insert('green water glass', 2, 17.3)
# insert('water glass', 5, 15)
# insert('coffee cup', 2, 30)
# delete('water glass');
update('coffee cup', 5, 35)
print(view())
