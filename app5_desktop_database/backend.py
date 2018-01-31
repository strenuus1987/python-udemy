import sqlite3

class Database:

    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.commit()

    def view_all(self):
        self.cursor.execute("SELECT * FROM books")
        res = self.cursor.fetchall()
        return res

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.commit()

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        res = self.cursor.fetchall()
        return res

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.commit()

    def commit(self):
        self.connect.commit()

    def __del__(self):
        self.connect.close()
