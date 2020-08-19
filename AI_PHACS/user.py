from tkinter import *


class User:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-PHACS | User Page")
        self.root.state('zoomed')
root = Tk()
obj = User(root)
root.mainloop()