from tkinter import *
from tkinter import messagebox
import pymysql
from cryptography.fernet import Fernet

class Main:

    def __init__(self, root):
        print(root)
        self.root = root
        self.root.title("AI-PHACS | Developed By : Sudip, Ayush, Bhavyesh, Preet, Jay | MiniDeveloper")
        # self.root.geometry('1200x900')
        self.root.state('zoomed')
        self.root.minsize()

        self.create_widgets()

    def close(self):
        root.destroy()

    def create_widgets(self):
        self.AdminPhoto = PhotoImage(file="images/Admin.png", master=self.root)
        self.UserPhoto = PhotoImage(file="images/User2.png", master=self.root)

        ## Variables
        self.user_id_var = StringVar()
        self.user_pass_var = StringVar()
        self.admin_id_var = StringVar()
        self.admin_pass_var = StringVar()

        # banner frame
        banner_frame = Frame(self.root, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Home Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.normal_user = Button(root, image=self.UserPhoto, font=("times new roman", 15, 'bold'), bg=None, border=0
                                  , cursor='hand2', command=self.user_window)
        self.normal_user.place(relx=0.4, rely=0.5, anchor=CENTER, width=430, height=200)

        self.admin = Button(root, image=self.AdminPhoto, font=("times new roman", 15, 'bold'), bg=None, border=0,
                            cursor='hand2', command=self.admin_window)
        self.admin.place(relx=0.6, rely=0.5, anchor=CENTER, width=430, height=200)

    def user_window(self):

        self.root.withdraw()
        self.user = Toplevel(root)

        self.user.title("AI-PHACS | User Login Page")
        self.user.state('zoomed')
        # self.user.geometry("1000x900")
        self.bg = PhotoImage(file="images/login-page-background.png", master=self.user)
        self.bg_image = Label(self.user, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.back = PhotoImage(file="images/back.png", master=self.user)

        # import user_login
        # print(user)
        backButton = Button(self.user, image=self.back, command=self.user_backClicked, border=0, height=60,
                            width=60, cursor='hand2', )
        backButton.place(x=20, y=90)

        # banner frame
        banner_frame = Frame(self.user, bg='white', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='USER Login Page', font=('Impact', 20, 'bold'), bg='white',
                             fg='#d77337')
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
        self.id_field = Entry(login_frame, textvariable=self.user_id_var, font=('times new roman', 15), bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)

        password = Label(login_frame, text='Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                         bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(login_frame, textvariable=self.user_pass_var, show="*",
                                    font=('times new roman', 15), bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(login_frame, text='Forget Password?', bg='white', fg='#d77337', bd=0,
                            font=('times new roman', 15), cursor='hand2')
        forget_btn.place(x=90, y=290)

        login_btn = Button(login_frame, text='Submit', bg='#d77337', fg='white',
                           font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
                           cursor='hand2', command=self.user_submit_clicked)
        login_btn.place(x=90, y=350, width=100, height=35)
        self.user.protocol("WM_DELETE_WINDOW", self.close)

    def admin_window(self):
        self.root.withdraw()

        self.admin = Toplevel(root)
        self.admin.title("AI-PHACS | Admin Login Page")
        self.admin.state('zoomed')
        self.bg = PhotoImage(file="images/login-page-background.png", master=self.admin)
        self.bg_image = Label(self.admin, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.back = PhotoImage(file="images/back.png", master=self.admin)
        backButton = Button(self.admin, image=self.back, command=self.admin_backClicked, border=0, height=60,
                            width=60, cursor='hand2', )
        backButton.place(x=20, y=90)

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
        self.id_field = Entry(login_frame, textvariable=self.admin_id_var, font=('times new roman', 15), bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)

        password = Label(login_frame, text='Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                         bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(login_frame, textvariable=self.admin_pass_var, show="*",
                                    font=('times new roman', 15), bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(login_frame, text='Forget Password?', bg='white', fg='#d77337', bd=0,
                            cursor='hand2', font=('times new roman', 15))
        forget_btn.place(x=90, y=290)

        login_btn = Button(login_frame, text='Submit', bg='#d77337', fg='white',
                           font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
                           cursor='hand2', command=self.admin_submit_clicked)
        login_btn.place(x=90, y=350, width=100, height=35)
        self.admin.protocol("WM_DELETE_WINDOW", self.close)

    def user_backClicked(self):
        self.user.withdraw()
        self.root.deiconify()
        self.root.state('zoomed')

    def admin_backClicked(self):
        self.admin.withdraw()
        self.root.deiconify()
        self.root.state('zoomed')

    def user_submit_clicked(self):
        # check if user is Authorized OR Not!!
        if self.id_field.get() == "" or self.password_field.get() == "":

            messagebox.showerror("Error", "All Fields Are Required!!", parent=self.user)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
                cursor = con.cursor()

                if cursor.execute(
                        "select username,password from register where usertype=%s and username=%s and password=%s",
                        (
                                'Teacher',
                                self.id_field.get(),
                                self.password_field.get()
                        )):

                    cursor.execute("select reg_id from register where username=%s", self.id_field.get())
                    row_id = cursor.fetchall()
                    session_id = row_id[0][0]
                    # print(session_id)
                    self.root.destroy()
                    encoded_text = str(session_id).encode()
                    key = Fernet.generate_key()
                    print(key)
                    f = Fernet(key)
                    token = f.encrypt(encoded_text)
                    ans = f.decrypt(token)
                    print(ans.decode("utf-8"))
                    with open('session_id.txt', 'w') as f:
                        f.write(key.decode("utf-8"))
                        f.write("\n")
                        f.write(token.decode("utf-8"))



                    import user_page
                else:
                    messagebox.showerror("Error", "UserName Or Password is Incorrect", parent=self.user)
                    self.user_clear()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To: {str(ex)}", parent=self.user)
                self.user_clear()
            # print(cursor.execute("select username from register where usertype=%s and username=%s", ('Teacher', self.id_field.get())))
            # print(self.id_field.get(), self.password_field.get())

    def admin_submit_clicked(self):
        if self.id_field.get() == "" or self.password_field.get() == "":

            messagebox.showerror("Error", "All Fields Are Required!!", parent=self.admin)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
                cursor = con.cursor()
                if cursor.execute(
                        "select username,password from register where usertype=%s and username=%s and password=%s",
                        ('Admin', self.id_field.get(), self.password_field.get())):

                    cursor.execute("select reg_id from register where username=%s", self.id_field.get())
                    row_id = cursor.fetchall()
                    session_id = row_id[0][0]
                    print(session_id)
                    self.root.destroy()
                    encoded_text = str(session_id).encode()
                    key = Fernet.generate_key()
                    f = Fernet(key)
                    token = f.encrypt(encoded_text)
                    ans = f.decrypt(token)
                    print(ans.decode("utf-8"))
                    with open('session_id.txt', 'w') as f:
                        f.write(key.decode("utf-8"))
                        f.write("\n")
                        f.write(token.decode("utf-8"))

                    import admin_page
                else:

                    messagebox.showerror("Error", "AdminName Or Password is Incorrect", parent=self.admin)
                    self.admin_clear()

            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To: {str(ex)}", parent=self.admin)
                self.admin_clear()

    def user_clear(self):
        self.user_id_var.set('')
        self.user_pass_var.set('')

    def admin_clear(self):
        self.admin_id_var.set('')
        self.admin_pass_var.set('')


root = Tk()

print(root)

obj = Main(root)
# self.user.protocol("WM_DELETE_WINDOW", root.destroy)
# self.admin.protocol("WM_DELETE_WINDOW", root.destroy)
# root.protocol("WM_DELETE_WINDOW", obj.close)
root.mainloop()
