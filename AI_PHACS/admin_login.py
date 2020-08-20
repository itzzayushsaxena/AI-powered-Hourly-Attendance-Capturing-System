from tkinter import *
from tkinter import messagebox


class Admin_Login:
    def __init__(self, admin):
        self.admin = admin
        self.admin.title("AI-PHACS | Admin Login Page")
        self.admin.state('zoomed')
        self.bg=PhotoImage(file="images/login-page-background.png")
        self.bg_image=Label(self.admin, image=self.bg).place(x=0 , y=0, relwidth=1, relheight=1)

        self.back = PhotoImage(file="images/back.png")
        self.create_widgets()

    def create_widgets(self):
        backButton = Button(root, image=self.back, command=self.backClicked, border=0, height=190,
                            width=341)
        backButton.place(x=20, y=50)

        #login_Frame
        login_frame=Frame(self.admin, bg='white', )
        login_frame.place(x=150, y=200, height=450, width=500)


        title=Label(login_frame, text='LogIn', font=('Impact', 35, 'bold'),  bg='white', fg='#d77337')
        title.place(x=180, y=30)


        desc = Label(login_frame, text='Admin Login Here', font=('Goudy old style', 15, 'bold'),  bg='white',
                     fg='#d25d17')
        desc.place(x=150, y=100)


        user_id = Label(login_frame, text='AdminName', font=('Goudy old style', 15, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=90, y=140)
        self.id_field=Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)


        password = Label(login_frame, text='Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                        bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(login_frame, font=('times new roman', 15), bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        forget_btn=Button(login_frame, text='Forget Password?', bg='white', fg='#d77337', bd=0, font=('times new roman', 15))
        forget_btn.place(x=90, y=290)


        login_btn = Button(login_frame, text='Submit', bg='#d77337', fg='white',
                            font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
                           command=self.submit_clicked)
        login_btn.place(x=90, y=350, width=100, height=35)

    def submit_clicked(self):
        # if true:
        #     self.admin.destroy()
        #     import admin_page
        # else:
        #     messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")
        self.admin.destroy()
        import admin_page

    def backClicked(self):
        self.admin.destroy()
        import main

root = Tk()
obj = Admin_Login(root)
root.mainloop()