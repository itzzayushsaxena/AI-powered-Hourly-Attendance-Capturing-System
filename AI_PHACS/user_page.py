from tkinter import *


class User_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-PHACS | User Page")
        self.root.state('zoomed')
        self.create_widgets()

    def create_widgets(self):
        self.back = PhotoImage(file="images/back.png")

        backButton = Button(self.root, image=self.back, command=self.user_page_backClicked, border=0, height=60,
                            width=60, cursor='hand2', )
        backButton.place(x=20, y=70)


        banner_frame = Frame(self.root, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='User Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

    def user_page_backClicked(self):
        self.root.destroy()
        import main


root = Tk()
obj = User_Page(root)
root.mainloop()