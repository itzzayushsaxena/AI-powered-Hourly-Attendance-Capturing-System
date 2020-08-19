from tkinter import *


class Admin_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-PHACS | Admin Page")
        self.root.state('zoomed')
root = Tk()
obj = Admin_Page(root)
root.mainloop()