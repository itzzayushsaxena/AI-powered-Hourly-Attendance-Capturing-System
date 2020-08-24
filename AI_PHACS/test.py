from tkinter import *
from tkinter import ttk
import os


class Admin_Page:
    def __init__(self, root):


        self.root = root

        self.current_files = None


        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = os.path.expanduser("~")
        options['parent'] = root
        options['title'] = 'Select files to annotate.'

        self.file_selector_button = ttk.Button(self.root, text=u"select file(s)", )
        self.label = ttk.Label(self.root, text=u"selected file(s):")
        self.fa_search = PhotoImage(
            file=os.path.join(self.root.resource_dir, "images", "fa_search_24_24.gif"))
        self.file_selector_button.config(image=self.fa_search, compound=LEFT)

        self.scrollbar = ttk.Scrollbar(self.root)
        self.selected_files = Listbox(self.root, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.selected_files.yview)

root = Tk()
obj = Admin_Page(root,)
root.mainloop()