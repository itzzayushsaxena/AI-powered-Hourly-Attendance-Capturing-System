from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import pymysql
import datetime


class Admin_Page:
    def __init__(self, root):
        self.admin_page = root
        self.admin_page.title("AI-PHACS | Admin Page")
        self.admin_page.state('zoomed')
        self.create_widgets()

    def create_widgets(self):
        self.trainingPhoto = PhotoImage(file="images/Start Training2.png", master=self.admin_page)
        self.studentPhoto = PhotoImage(file="images/Add Student2.png", master=self.admin_page)
        self.userPhoto = PhotoImage(file="images/Add User2.png", master=self.admin_page)
        self.detailPhoto = PhotoImage(file="images/Check Details2.png", master=self.admin_page)
        self.attendancePhoto = PhotoImage(file="images/Check Attendance2.png", master=self.admin_page)
        self.logoutPhoto = PhotoImage(file="images/logout4.png", master=self.admin_page)



        # banner frame
        self.banner_frame = Frame(self.admin_page, bg='#49a0ae', )
        self.banner_frame.place(x=310,relwidth=1, y=0, height=50)
        self.banner_title = Label(self.banner_frame, text='Admin | Add Student Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        logout_label = Label(self.banner_frame, text='Logout ', font=('times new roman', 12, 'bold'), bg='#49a0ae', fg='white')
        logout_label.place(x=940, y=15)
        # logout_frame = Frame(self.banner_frame, bg='black', )
        # logout_frame.place(x=930, y=5, width=40,  height= 40)
        logoutButton = Button(self.banner_frame, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=45,
                              width=45, cursor='hand2', bg='#49a0ae', activebackground='#49a0ae',)
        logoutButton.place(x=990, y=5)

        ###### FRAMES

        self.btn_frame = Frame(self.admin_page, bg=None)
        self.btn_frame.place(x=5, relheight=1, width=300)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=310,  y=55, height=680, width=1050)

        self.draw_add_student()



    def draw_add_student(self):


        self.addStudentButton = Button(self.btn_frame, image=self.studentPhoto, command=self.addStudentClicked, border=0,
                                  height=140,
                                  width=341, cursor='hand2', state='disable', )
        self.addStudentButton.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.trainButton = Button(self.btn_frame, image=self.trainingPhoto, command=self.trainButtonClicked, border=0,
                             height=140, width=341, cursor='hand2', )
        self.trainButton.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.checkDetailButton = Button(self.btn_frame, image=self.detailPhoto, command=self.checkDetailClicked, border=0,
                                   height=140, width=341, cursor='hand2', )
        self.checkDetailButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.addUserButton = Button(self.btn_frame, image=self.userPhoto, command=self.addUserClicked, border=0,
                               height=140, width=341, cursor='hand2', )
        self.addUserButton.place(relx=0.5, rely=0.70, anchor=CENTER)

        self.checkAttendanceButton = Button(self.btn_frame, image=self.attendancePhoto, command=self.checkAttendanceClicked,
                                       border=0,
                                       height=140, width=341, cursor='hand2', )
        self.checkAttendanceButton.place(relx=0.5, rely=0.90, anchor=CENTER)


        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'



    def addStudentClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()
        self.banner_title = Label(self.banner_frame, text='Admin | Add Student Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.addStudentButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'

#### ============================================= Training           =============================================#####
#### ==============================================================================================================#####
    def trainButtonClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | Training Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.trainButton['state'] = 'disable'
        self.checkAttendanceButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'

#### ============================================= Check Detail       =============================================#####
#### ==============================================================================================================#####

    def checkDetailClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | Check Detail Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.checkDetailButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'


#### ============================================= USER REGISTRATION  =============================================#####
#### ==============================================================================================================#####


    def addUserClicked(self):
        self.changeable_frame.destroy()

        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | ADD User Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg=None)
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.addUserButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'
        self.draw_add_user()

    def draw_add_user(self):
        self.manage_user_frame = Frame(self.changeable_frame, bg='white')
        self.manage_user_frame.place(x=5, y=5, width=1040, height=130)

        self.user_data_frame = Frame(self.changeable_frame, bg='white')
        self.user_data_frame.place(x=5, y=140, width=1040, height=545)

        ###Variables
        self.user_id_var = StringVar()
        self.user_pass_var = StringVar()
        self.searchby_usertype_var = StringVar()

        sub_banner_title = Label(self.manage_user_frame, text='Manage User', font=('Impact', 30, 'bold'), bg='white',
                                 fg='#49a0ae')
        sub_banner_title.place(relx=0.15, rely=0.3, anchor=CENTER)

        user_id = Label(self.manage_user_frame, text='Set UserName', font=('Goudy old style', 12, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=350, y=15)
        self.id_field = Entry(self.manage_user_frame, textvariable=self.user_id_var, font=('times new roman', 12),
                              bg='lightgray')
        self.id_field.place(x=350, y=50, width=200, height=22)

        password = Label(self.manage_user_frame, text='Set Password', font=('Goudy old style', 12, 'bold'), fg='gray',
                         bg='white')
        password.place(x=585, y=15)
        self.password_field = Entry(self.manage_user_frame, textvariable=self.user_pass_var, font=('times new roman', 12),
                                    bg='lightgray')
        self.password_field.place(x=585, y=50, width=200, height=22)

        user_type = Label(self.manage_user_frame, text='User Type', font=('Goudy old style', 12, 'bold'), fg='gray',
                          bg='white')
        user_type.place(x=820, y=15)
        self.user_type_combox = ttk.Combobox(self.manage_user_frame, font=('times new roman', 12), state='readonly')
        self.user_type_combox['values'] = ("Admin", "Teacher")
        self.user_type_combox.place(x=820, y=50, width=150, height=22)

        # button_frame

        self.btn_frame = Frame(self.manage_user_frame, bg='white', )
        self.btn_frame.place(relwidth=1, y=250, height=50)
        add_btn = Button(self.manage_user_frame, text='Add User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.add_user_submit_clicked)
        add_btn.place(x=400, y=85, width=100, height=30)

        del_btn = Button(self.manage_user_frame, text='Delete User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.delete_data)
        del_btn.place(x=520, y=85, width=100, height=30)

        edit_btn = Button(self.manage_user_frame, text='Update Data', bg='#49a0ae', fg='white',
                          font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                          cursor='hand2', command=self.update_data)
        edit_btn.place(x=640, y=85, width=100, height=30)

        clr_btn = Button(self.manage_user_frame, text='Clear Data', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.clear)
        clr_btn.place(x=760, y=85, width=100, height=30)

        # data frame


        data_banner_frame = Frame(self.user_data_frame, bg='#49a0ae', )
        data_banner_frame.place(relwidth=1, y=0, height=50)
        data_banner_title = Label(data_banner_frame, text='User Data', font=('times new roman', 20, 'bold'), bg='#49a0ae',
                                  fg='white')
        data_banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)
        #search_Frame

        self.search_frame = Frame(self.user_data_frame, bg='white', )
        self.search_frame.place(relwidth=1, y=55, height=50)

        search = Label(self.search_frame, text='Search By :', font=('times new roman', 12), bg='white',
                       fg='black')
        search.place(x=30, y=10)

        user_type = Label(self.search_frame, text='User Type', font=('Goudy old style', 12), fg='gray',
                          bg='white')
        user_type.place(x=170, y=10)
        self.search_user_type_combox = ttk.Combobox(self.search_frame, textvariable=self.searchby_usertype_var,
                                                    font=('times new roman', 12), state='readonly')
        self.search_user_type_combox['values'] = ("Admin", "Teacher")
        self.search_user_type_combox.place(x=280, y=10, width=100, height=22, )

        search_btn = Button(self.search_frame, text='Search', bg='#49a0ae', fg='white',
                            font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.search)
        search_btn.place(x=400, y=10, width=60, height=22)

        show_all_btn = Button(self.search_frame, text='Show All', bg='#49a0ae', fg='white',
                              font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                              cursor='hand2', command=self.fetch_data)
        show_all_btn.place(x=490, y=10, width=60, height=22)

        # Table Frame
        table_frame = Frame(self.user_data_frame, bd=4, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=110, width=1025, height=430)

        scroll_horizon = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(table_frame, orient=VERTICAL)
        self.data_table = ttk.Treeview(table_frame, columns=("no", "id", "doj", "type"),
                                       xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.data_table.xview)
        scroll_vertical.config(command=self.data_table.yview)
        self.data_table.heading("no", text="No.")
        self.data_table.column("no", width=90)
        self.data_table.heading("id", text="User Name")
        self.data_table.column("id", width=250)
        self.data_table.heading("doj", text="Date Of Joining")
        self.data_table.column("doj", width=150)
        self.data_table.heading("type", text="User Type")
        self.data_table['show'] = 'headings'
        self.data_table.pack(fill=BOTH, expand=1)

        ##get the selected data from table to fields.
        self.data_table.bind('<ButtonRelease-1>', self.get_selection)

        ##fetch data from register

        self.fetch_data()

    def add_user_submit_clicked(self):
        if self.id_field.get() == '' or self.user_type_combox.get() == '' or self.password_field.get() == '':
            messagebox.showerror("Error", "All field Are Required To Add User", parent=self.manage_user_frame)
        else:
            # try:
            # print(self.id_field.get(), self.password_field.get(), self.user_type_combox.get(), datetime.datetime.now().strftime('%Y-%m-%d'))
            con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
            cursor = con.cursor()
            if cursor.execute("select username from register where username=%s", self.id_field.get()):
                messagebox.showerror("Error", "User Already Exist, Try Different Username")
            else:
                cursor.execute("insert into register(username,date,usertype,password) values(%s,%s,%s,%s)",
                               (
                                   self.id_field.get(),
                                   datetime.datetime.now().strftime('%Y-%m-%d'),
                                   self.user_type_combox.get(),
                                   self.password_field.get()
                               ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                ### base64.b64encode (pass)
                ### base64.b64decode (pass)
            # except Exception as ex:
            #
            #     messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}\n User Already Exist, Try Different Username")
            #     self.clear()

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
        cursor = con.cursor()
        cursor.execute("select * from register")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.user_id_var.set('')
        self.user_type_combox.set('')
        self.user_pass_var.set('')

    # event will contain the object of action
    def get_selection(self, event):
        selection_row = self.data_table.focus()
        contents = self.data_table.item(selection_row)
        self.row = contents['values']
        # print(row)
        self.user_id_var.set(self.row[1])
        self.user_type_combox.set(self.row[3])
        self.user_pass_var.set(self.row[4])

    def update_data(self):

        if self.id_field.get() == '' or self.user_type_combox.get() == '' or self.password_field.get() == '':
            messagebox.showerror("Error", "Select User From Table To Update", parent=self.manage_user_frame)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
                cursor = con.cursor()
                cursor.execute("update register set username=%s, date=%s, usertype=%s, password=%s where reg_id=%s",
                               (
                                   self.id_field.get(),
                                   datetime.datetime.now().strftime('%Y-%m-%d'),
                                   self.user_type_combox.get(),
                                   self.password_field.get(),
                                   self.row[0]
                               ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}\n Select User From Table To Update")
                self.clear()

    def delete_data(self):
        if self.id_field.get() == '' or self.user_type_combox.get() == '' or self.password_field.get() == '':
            messagebox.showerror("Error", "Select User From Table To Delete", parent=self.manage_user_frame)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
                cursor = con.cursor()
                cursor.execute("delete from register where reg_id=%s", self.row[0])
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}\n Select User From Table To Delete")
                self.clear()

    def search(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
        cursor = con.cursor()
        cursor.execute("select * from register where usertype=%s", self.searchby_usertype_var.get())
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert('', END, values=row)
            con.commit()
        con.close()

#### ============================================= CHECK ATTENDANCE  =============================================######
#### ==============================================================================================================#####

    def checkAttendanceClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | Check Attendance Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.checkAttendanceButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'
        print('sucess')

#### ============================================= LOG OUT  =============================================######
#### ==============================================================================================================#####
    def logoutClicked(self):
        self.admin_page.destroy()
        import main
root = Tk()
obj = Admin_Page(root)
root.mainloop()