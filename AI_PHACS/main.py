from tkinter import *
from tkinter import messagebox

class Main:


    def __init__(self,root):
        print(root)
        self.root=root
        self.root.title("AI-PHACS | Developed By : Sudip, Ayush, Bhavyesh, Preet, Jay | MiniDeveloper")
        # self.root.geometry('1200x900')
        self.root.state('zoomed')
        self.root.minsize()
        self.create_widgets()

    def create_widgets(self):

        #banner frame
        banner_frame = Frame(self.root, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Home Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.normal_user = Button(root, text="USER",font=("times new roman", 15, 'bold'), bg='#49a0ae', fg='white',
                                  activebackground='#49a0ae', activeforeground='white', cursor='hand2',
                                  command=self.user_window)
        self.normal_user.place(relx=0.4, rely=0.5, anchor=CENTER,width=100,height=80)


        self.admin = Button(root, text="Admin", font=("times new roman", 15, 'bold'), bg='#49a0ae', fg='white',
                            activebackground='#49a0ae', activeforeground='white', cursor='hand2',
                            command=self.admin_window)
        self.admin.place(relx=0.6, rely=0.5, anchor=CENTER,width=100,height=80)

    def user_window(self):


        self.user = Toplevel(root)

        self.user.title("AI-PHACS | User Login Page")
        # self.user.state('zoomed')
        self.user.geometry("1000x900")
        self.bg = PhotoImage(file="images/login-page-background.png")
        self.bg_image = Label(self.user, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.back = PhotoImage(file="images/back.png")

        # import user_login
        # print(user)
        # backButton = Button(user, image=self.back, command=self.backClicked, border=0, height=190,
        #                     width=341)
        # backButton.place(x=20, y=50)

        # banner frame
        banner_frame = Frame(self.user, bg='white', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='USER Login Page', font=('Impact', 20, 'bold'), bg='white', fg='#d77337')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        # login_Frame
        login_frame = Frame(self.user, bg='white', )
        login_frame.place(x=150, y=200, height=450, width=500)

        title = Label(login_frame, text='LogIn', font=('Impact', 35, 'bold'), bg='white', fg='#d77337')
        title.place(x=180, y=30)

        desc = Label(login_frame, text='User Login Here', font=('Goudy old style', 15, 'bold'), bg='white',
                     fg='#d25d17')
        desc.place(x=150, y=100)

        user_id = Label(login_frame, text='UserName', font=('Goudy old style', 15, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=90, y=140)
        self.id_field = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)

        password = Label(login_frame, text='Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                         bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(login_frame, text='Forget Password?', bg='white', fg='#d77337', bd=0,
                            font=('times new roman', 15))
        forget_btn.place(x=90, y=290)

        login_btn = Button(login_frame, text='Submit', bg='#d77337', fg='white',
                           font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
                           command=self.user_submit_clicked)
        login_btn.place(x=90, y=350, width=100, height=35)

    def admin_window(self):
        try:

            if 'normal' == self.user.state():
                self.user.destroy()
        except:
            # messagebox.showerror("Error", "Close Opened Window First.")
            self.admin = Toplevel(root)
            self.admin.title("AI-PHACS | Admin Login Page")
            # self.admin.state('zoomed')
            self.admin.geometry("1000x900")
            self.bg = PhotoImage(file="images/login-page-background.png")
            self.bg_image = Label(self.admin, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

            # self.back = PhotoImage(file="images/back.png")
            # backButton = Button(root, image=self.back, command=self.backClicked, border=0, height=190,
            #                     width=341)
            # backButton.place(x=20, y=50)

            # banner frame
            banner_frame = Frame(self.admin, bg='white', )
            banner_frame.place(relwidth=1, y=0, height=50)
            banner_title = Label(banner_frame, text='ADMIN Login Page', font=('Impact', 20, 'bold'), bg='white',
                                 fg='#d77337')
            banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

            # login_Frame
            login_frame = Frame(self.admin, bg='white', )
            login_frame.place(x=150, y=200, height=450, width=500)

            title = Label(login_frame, text='LogIn', font=('Impact', 35, 'bold'), bg='white', fg='#d77337')
            title.place(x=180, y=30)

            desc = Label(login_frame, text='Admin Login Here', font=('Goudy old style', 15, 'bold'), bg='white',
                         fg='#d25d17')
            desc.place(x=150, y=100)

            user_id = Label(login_frame, text='AdminName', font=('Goudy old style', 15, 'bold'), fg='gray',
                            bg='white')
            user_id.place(x=90, y=140)
            self.id_field = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
            self.id_field.place(x=90, y=170, width=350, height=35)

            password = Label(login_frame, text='Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                             bg='white')
            password.place(x=90, y=210)
            self.password_field = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
            self.password_field.place(x=90, y=240, width=350, height=35)

            forget_btn = Button(login_frame, text='Forget Password?', bg='white', fg='#d77337', bd=0,
                                font=('times new roman', 15))
            forget_btn.place(x=90, y=290)

            login_btn = Button(login_frame, text='Submit', bg='#d77337', fg='white',
                               font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
                               command=self.admin_submit_clicked)
            login_btn.place(x=90, y=350, width=100, height=35)

    def user_submit_clicked(self):
        # if true:
        #     self.user.destroy()
        #     import user_page
        # else:
        #     messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")
        self.root.destroy()
        import user_page

    def admin_submit_clicked(self):
        # if true:
        #     self.user.destroy()
        #     import user_page
        # else:
        #     messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")
        self.root.destroy()
        import admin_page


root = Tk()
print(root)
obj = Main(root)
root.mainloop()