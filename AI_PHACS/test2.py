# ListBox Widget

from tkinter import *


def apply():
    print(lb.curselection())

master = Tk()

lb = Listbox(master, selectmode=MULTIPLE)
lb.pack()

lb.insert(END, "a list entry")

data = ["one", "two", "three", "four"]

for item in data:
    lb.insert(END, item)

# items = map(int, lb.curselection())
# items = lb.curselection()
# items = [data[int(item)] for item in items]
apply_btn = Button(master, text='Update', bg='#49a0ae', fg='white',
                           font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                           cursor='hand2', command=apply)
apply_btn.place(x=100, y=330, width=70, height=18)

mainloop()