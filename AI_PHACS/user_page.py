from tkinter import *


class User_Page:
    def __init__(self, root):
        self.user_page = root
        self.user_page.title("AI-PHACS | User Page")
        self.user_page.state('zoomed')
        self.create_widgets()

    def create_widgets(self):

        self.logoutPhoto = PhotoImage(file="images/logout.png", master=self.user_page)

        logout_label = Label(self.user_page, text='Logout ', font=('Impact', 20, 'bold'), bg=None, fg='gray')
        logout_label.place(x=1100, y=80)
        logoutButton = Button(self.user_page, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=60,
                              width=60, cursor='hand2', )
        logoutButton.place(x=1200, y=70)


        banner_frame = Frame(self.user_page, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='User Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

    def logoutClicked(self):
        self.user_page.destroy()
        import main


root = Tk()
obj = User_Page(root)
root.mainloop()