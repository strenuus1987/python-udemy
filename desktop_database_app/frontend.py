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
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        e_title.delete(0, END)
        e_title.insert(END, selected_tuple[1])
        e_author.delete(0, END)
        e_author.insert(END, selected_tuple[2])
        e_year.delete(0, END)
        e_year.insert(END, selected_tuple[3])
        e_isbn.delete(0, END)
        e_isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list_box.delete(0, END)
    for row in backend.view_all():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in backend.search(var_title.get(), var_author.get(), var_year.get(), var_isbn.get()):
        list_box.insert(END, row)

def add_command():
    backend.insert(var_title.get(), var_author.get(), var_year.get(), var_isbn.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0], var_title.get(), var_author.get(), var_year.get(), var_isbn.get())
    view_command()

window = Tk()
window.title("Books database")

l_title=Label(window, text="Title")
l_title.grid(row=0, column=0)

l_year=Label(window, text="Year")
l_year.grid(row=1, column=0)

l_author=Label(window, text="Author")
l_author.grid(row=0, column=2)

l_isbn=Label(window, text="ISBN")
l_isbn.grid(row=1, column=2)

var_title = StringVar()
e_title = Entry(window, textvariable=var_title)
e_title.grid(row=0, column=1)

var_year = StringVar()
e_year = Entry(window, textvariable=var_year)
e_year.grid(row=1, column=1)

var_author = StringVar()
e_author = Entry(window, textvariable=var_author)
e_author.grid(row=0, column=3)

var_isbn = StringVar()
e_isbn = Entry(window, textvariable=var_isbn)
e_isbn.grid(row=1, column=3)

list_box = Listbox(window, height=8, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6, sticky='ns')

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

button_view_all = Button(window, text="View all", width=12, command=view_command)
button_view_all.grid(row=2, column=3)

button_search = Button(window, text="Search entry", width=12, command=search_command)
button_search.grid(row=3, column=3)

button_add = Button(window, text="Add entry", width=12, command=add_command)
button_add.grid(row=4, column=3)

button_update = Button(window, text="Update", width=12, command=update_command)
button_update.grid(row=5, column=3)

button_delete = Button(window, text="Delete", width=12, command=delete_command)
button_delete.grid(row=6, column=3)

button_close = Button(window, text="Close", width=12, command=window.destroy)
button_close.grid(row=7, column=3)

window.mainloop()
