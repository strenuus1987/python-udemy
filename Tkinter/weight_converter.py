from tkinter import *

def weight_convert():
    t_grams.delete(1.0, END)
    t_pounds.delete(1.0, END)
    t_ounces.delete(1.0, END)
    t_grams.insert(END, float(entry_val.get())*1000)
    t_pounds.insert(END, float(entry_val.get())*2.20462)
    t_ounces.insert(END, float(entry_val.get())*35.274)

window = Tk()

label = Label(window, text="Kg")
label.grid(row=0, column=0)

entry_val = StringVar()
entry = Entry(window, textvariable=entry_val)
entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=weight_convert)
button.grid(row=0, column=2)

t_grams = Text(window, height=1, width=15)
t_grams.grid(row=1, column=0)

t_pounds = Text(window, height=1, width=15)
t_pounds.grid(row=1, column=1)

t_ounces = Text(window, height=1, width=15)
t_ounces.grid(row=1, column=2)

window.mainloop()
