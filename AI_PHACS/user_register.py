from tkinter import *


class User_Register:

    def __init__(self, root):
        self.add_user = root
        self.add_user.title("AI-PHACS | User Registration")
        self.add_user.state('zoomed')
        self.back = PhotoImage(file="images/back.png")
        self.create_widgets()

    def create_widgets(self):


        backButton = Button(self.add_user, image=self.back, command=self.backClicked, border=0, height=60,
                            width=60, cursor='hand2', )
        backButton.place(x=20, y=90)

        # banner frame
        banner_frame = Frame(self.add_user, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Manage User Page', font=('Impact', 20, 'bold'), bg='white',
                             fg='#d77337')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)


    def backClicked(self):
        self.add_user.destroy()
        # self.root.deiconify()
        # self.root.state('zoomed')


root = Tk()
obj = User_Register(root)
root.mainloop()