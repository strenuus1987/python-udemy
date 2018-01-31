"""
A program that stores this book information
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete entry
Close
"""
from tkinter import *
from backend import Database

class MainWindow():

    def __init__(self, database):

        self.database = database

        self.window = Tk()
        self.window.title("Books database")

        self.l_title=Label(self.window, text="Title")
        self.l_title.grid(row=0, column=0)

        self.l_year=Label(self.window, text="Year")
        self.l_year.grid(row=1, column=0)

        self.l_author=Label(self.window, text="Author")
        self.l_author.grid(row=0, column=2)

        self.l_isbn=Label(self.window, text="ISBN")
        self.l_isbn.grid(row=1, column=2)

        self.var_title = StringVar()
        self.e_title = Entry(self.window, textvariable=self.var_title)
        self.e_title.grid(row=0, column=1)

        self.var_year = StringVar()
        self.e_year = Entry(self.window, textvariable=self.var_year)
        self.e_year.grid(row=1, column=1)

        self.var_author = StringVar()
        self.e_author = Entry(self.window, textvariable=self.var_author)
        self.e_author.grid(row=0, column=3)

        self.var_isbn = StringVar()
        self.e_isbn = Entry(self.window, textvariable=self.var_isbn)
        self.e_isbn.grid(row=1, column=3)

        self.list_box = Listbox(self.window, height=8, width=35)
        self.list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.grid(row=2, column=2, rowspan=6, sticky='ns')

        self.list_box.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.list_box.yview)

        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        self.button_view_all = Button(self.window, text="View all", width=12, command=self.view_command)
        self.button_view_all.grid(row=2, column=3)

        self.button_search = Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.button_search.grid(row=3, column=3)

        self.button_add = Button(self.window, text="Add entry", width=12, command=self.add_command)
        self.button_add.grid(row=4, column=3)

        self.button_update = Button(self.window, text="Update", width=12, command=self.update_command)
        self.button_update.grid(row=5, column=3)

        self.button_delete = Button(self.window, text="Delete", width=12, command=self.delete_command)
        self.button_delete.grid(row=6, column=3)

        self.button_close = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.button_close.grid(row=7, column=3)

        self.window.mainloop()

    def get_selected_row(self, event):
        try:
            index = self.list_box.curselection()[0]
            self.selected_tuple = self.list_box.get(index)
            self.e_title.delete(0, END)
            self.e_title.insert(END, self.selected_tuple[1])
            self.e_author.delete(0, END)
            self.e_author.insert(END, self.selected_tuple[2])
            self.e_year.delete(0, END)
            self.e_year.insert(END, self.selected_tuple[3])
            self.e_isbn.delete(0, END)
            self.e_isbn.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def clear_list(self):
        self.list_box.delete(0, END)

    def view_command(self):
        self.clear_list()
        for row in self.database.view_all():
            self.list_box.insert(END, row)

    def search_command(self):
        self.clear_list()
        for row in self.database.search(self.var_title.get(), self.var_author.get(), self.var_year.get(), self.var_isbn.get()):
            self.list_box.insert(END, row)

    def add_command(self):
        self.database.insert(self.var_title.get(), self.var_author.get(), self.var_year.get(), self.var_isbn.get())
        self.view_command()

    def delete_command(self):
        self.database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        self.database.update(self.selected_tuple[0], self.var_title.get(), self.var_author.get(), self.var_year.get(), self.var_isbn.get())
        self.view_command()

window = MainWindow(Database('database.db'))
