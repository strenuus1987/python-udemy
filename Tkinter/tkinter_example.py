from tkinter import *

def km_to_miles():
    t1.insert(END, float(e1_val.get())*1.6)

window = Tk()

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=0)

b1 = Button(window, text="Execute", command=km_to_miles)
#b1.pack()
b1.grid(row=0, column=1)

t1 = Text(window, height=2, width=23)
t1.grid(row=1, column=0, columnspan=2)

window.mainloop()
