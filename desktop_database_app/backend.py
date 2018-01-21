import sqlite3

def create_table():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connect.commit()
    connect.close()

def view_all():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books")
    res = cursor.fetchall()
    connect.close()
    return res

def insert(title, author, year, isbn):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    connect.commit()
    connect.close()

def search(title="", author="", year="", isbn=""):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    res = cursor.fetchall()
    connect.close()
    return res

def delete(id):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    connect.commit()
    connect.close()

def update(id, title, author, year, isbn):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connect.commit()
    connect.close()

create_table()
