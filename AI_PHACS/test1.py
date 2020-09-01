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
        self.trainingPhoto = PhotoImage(file="images/Add Timetable3.png", master=self.admin_page)
        self.studentPhoto = PhotoImage(file="images/Add Timetable3.png", master=self.admin_page)
        self.userPhoto = PhotoImage(file="images/Add Timetable3.png", master=self.admin_page)
        self.detailPhoto = PhotoImage(file="images/Add Timetable3.png", master=self.admin_page)
        self.attendancePhoto = PhotoImage(file="images/Add Timetable3.png", master=self.admin_page)
        self.logoutPhoto = PhotoImage(file="images/logout4.png", master=self.admin_page)



        # banner frame
        self.banner_frame = Frame(self.admin_page, bg='#49a0ae', )
        self.banner_frame.place(x=155, relwidth=1, y=0, height=50)
        self.banner_title = Label(self.banner_frame, text='Admin | Add Student Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        logout_label = Label(self.banner_frame, text='Logout ', font=('times new roman', 12, 'bold'), bg='#49a0ae', fg='white')
        logout_label.place(x=1100, y=15)
        # logout_frame = Frame(self.banner_frame, bg='black', )
        # logout_frame.place(x=930, y=5, width=40,  height= 40)
        logoutButton = Button(self.banner_frame, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=45,
                              width=45, cursor='hand2', bg='#49a0ae', activebackground='#49a0ae',)
        logoutButton.place(x=1150, y=5)

        ###### FRAMES

        self.btn_frame = Frame(self.admin_page, bg=None)
        self.btn_frame.place(x=5, relheight=1, width=150)

        self.changeable_frame = Frame(self.admin_page, bg='white')
        self.changeable_frame.place(x=310,  y=55, height=680, width=1050)

        self.admin_template()



    def admin_template(self):
        # sep = ttk.Separator(self.btn_frame).place(x=0, y=100, relwidth=1)
        # sep.pack(side="left", fill="x", padx=4, pady=4, expand=1)
        # sep = ttk.Style()
        # sep.configure('TSeparator', background='black')

        self.checkAttendanceButton = Button(self.btn_frame, image=self.attendancePhoto,
                                            command=self.checkAttendanceClicked,
                                            border=0,
                                            height=100, width=100, cursor='hand2',)
        self.checkAttendanceButton.place(relx=0.5, rely=0.1, anchor=CENTER)


        self.addUserButton = Button(self.btn_frame, image=self.userPhoto, command=self.addUserClicked, border=0,
                                    height=100, width=100, cursor='hand2', )
        self.addUserButton.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.addStudentButton = Button(self.btn_frame, image=self.studentPhoto, command=self.draw_add_student, border=0,
                                  height=100,
                                  width=100, cursor='hand2', state='disable', )
        self.addStudentButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.trainButton = Button(self.btn_frame, image=self.trainingPhoto, command=self.trainButtonClicked, border=0,
                             height=100, width=100, cursor='hand2', )
        self.trainButton.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.checkDetailButton = Button(self.btn_frame, image=self.detailPhoto, command=self.checkDetailClicked,
                                        border=0,
                                        height=100, width=100, cursor='hand2', )
        self.checkDetailButton.place(relx=0.5, rely=0.9, anchor=CENTER)


        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.draw_add_student()


    def draw_add_student(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()
        self.banner_title = Label(self.banner_frame, text='Admin | Add Student Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.changeable_frame = Frame(self.admin_page, bg='white')
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

        self.addStudentButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'

        # s = ttk.Separator(self.changeable_frame, orient=VERTICAL)
        # s.pack(side=TOP, fill="y", padx=345, pady=177)

        ###Variables
        self.student_name_var = StringVar()
        self.enroll_no_var = StringVar()
        self.student_email_var = StringVar()
        self.dob_date_field_var = StringVar()
        self.dob_date_field_var.set('DD')
        self.dob_month_field_var = StringVar()
        self.dob_month_field_var.set('MM')
        self.dob_year_field_var = StringVar()
        self.dob_year_field_var.set('YYYY')
        self.student_gender_var = StringVar()
        self.phone_no_var = StringVar()
        self.student_address_var = StringVar()


        self.add_student_frame = Frame(self.changeable_frame, bg='white', bd=4, relief=RIDGE)
        self.add_student_frame.place(x=5, y=5, height=670, width=1190)
        self.upload_Photo = PhotoImage(file="images/student_image400.png", master=self.add_student_frame)

        student_name = Label(self.add_student_frame, text='Student Name ', font=('Goudy old style', 15, 'bold'),
                             fg='gray',
                             bg='white')
        student_name.place(x=135, y=60)
        self.name_field = Entry(self.add_student_frame, textvariable=self.student_name_var, font=('times new roman', 15), bg='lightgray')
        self.name_field.place(x=305, y=60, width=250, height=30)

        enroll_no = Label(self.add_student_frame, text='EnRoll No. ', font=('Goudy old style', 15, 'bold'),
                          fg='gray',
                          bg='white')
        enroll_no.place(x=135, y=120)
        self.enroll_no_field = Entry(self.add_student_frame, textvariable=self.enroll_no_var, font=('times new roman', 15), bg='lightgray')
        self.enroll_no_field.place(x=305, y=120, width=250, height=30)

        email = Label(self.add_student_frame, text='Email', font=('Goudy old style', 15, 'bold'),
                      fg='gray',
                      bg='white')
        email.place(x=135, y=200)
        self.email_field = Entry(self.add_student_frame, textvariable=self.student_email_var, font=('times new roman', 15), bg='lightgray')
        self.email_field.place(x=305, y=200, width=250, height=30)

        dob = Label(self.add_student_frame, text='Date Of Birth', font=('Goudy old style', 15, 'bold'),
                    fg='gray',
                    bg='white')
        dob.place(x=135, y=280)


        self.date_field = Entry(self.add_student_frame, textvariable=self.dob_date_field_var, font=('times new roman', 15), bg='lightgray')

        self.date_field.place(x=305, y=280, width=50, height=30)

        slash1 = Label(self.add_student_frame, text='/', font=('Goudy old style', 20), bg='white', fg='gray')
        slash1.place(x=365, y=276)
        self.month_field = Entry(self.add_student_frame, textvariable=self.dob_month_field_var, font=('times new roman', 15), bg='lightgray')
        self.month_field.place(x=385, y=280, width=50, height=30)
        slash2 = Label(self.add_student_frame, text='/', font=('Goudy old style', 20), bg='white', fg='gray')
        slash2.place(x=445, y=276)
        self.year_field = Entry(self.add_student_frame, textvariable=self.dob_year_field_var, font=('times new roman', 15), bg='lightgray')
        self.year_field.place(x=465, y=280, width=90, height=30)
        self.date_field.bind('<ButtonRelease-1>', self.date_selected)
        self.month_field.bind('<ButtonRelease-1>', self.month_selected)
        self.year_field.bind('<ButtonRelease-1>', self.year_selected)

        student_gender = Label(self.add_student_frame, text='Gender', font=('Goudy old style', 15, 'bold'), fg='gray',
                          bg='white')
        student_gender.place(x=135, y=360)
        self.student_gender_combox = ttk.Combobox(self.add_student_frame, font=('times new roman', 15), state='readonly')
        self.student_gender_combox['values'] = ("M", "F")
        self.student_gender_combox.place(x=305, y=360, width=250, height=30)

        phone_no = Label(self.add_student_frame, text='Phone Number', font=('Goudy old style', 15, 'bold'),
                         fg='gray',
                         bg='white')
        phone_no.place(x=135, y=420)
        self.phone_no_field = Entry(self.add_student_frame, textvariable=self.phone_no_var, font=('times new roman', 15), bg='lightgray')
        self.phone_no_field.place(x=305, y=420, width=250, height=30)

        address = Label(self.add_student_frame, text='Address', font=('Goudy old style', 15, 'bold'),
                        fg='gray',
                        bg='white')

        address.place(x=135, y=480)
        self.address_field = Text(self.add_student_frame, width=25, height=3, font=('times new roman', 15),
                             bg='lightgray')
        self.address_field.place(x=305, y=480)

        self.upload_image_frame = Frame(self.add_student_frame,  )
        self.upload_image_frame.place(x=700, y=110, height=360, width=320,)
        label = Label(self.upload_image_frame, image=self.upload_Photo, bg='white')
        label.pack()
        self.btn_border_frame = Frame(self.upload_image_frame, bg="#F97C14")
        upload_btn = Button(self.btn_border_frame, text='Upload Image', bd=0, fg='#F97C14',
                         font=('times new roman', 14, 'bold'), activebackground='#F97C14', activeforeground='white',
                         cursor='hand2', )
        upload_btn.pack(fill="both", expand=True, padx=1, pady=1)
        self.btn_border_frame.place(x=100, y=260, height=30, width=120)
        # canvas = Canvas(self.add_student_frame, width=300, height=340)
        # canvas.place(x=580, y=150)
        # canvas.create_image(0, 0, anchor=NW, image=self.upload_Photo)
        add_student_submit_btn = Button(self.add_student_frame, text='Add Student', bg='#49a0ae', fg='white',
                            font=('times new roman', 14, 'bold'), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.add_student_submit_clicked)
        add_student_submit_btn.place(x=495, y=575)
    def date_selected(self, event):
        self.dob_date_field_var.set('')
    def month_selected(self, event):
        self.dob_month_field_var.set('')
    def year_selected(self, event):
        self.dob_year_field_var.set('')

    def add_student_submit_clicked(self):
        if (self.name_field.get() == '' or self.enroll_no_field.get() == '' or self.student_gender_combox.get() == ''
                or self.dob_date_field_var.get() == '' or self.dob_month_field_var.get() == ''
                or self.dob_year_field_var.get() == '' or self.phone_no_field.get() == ''
                or self.address_field.get() == ''):
            messagebox.showerror("Error", "All field Are Required To Add Student", parent=self.add_student_frame)


#### ============================================= Training           =============================================#####
#### ==============================================================================================================#####
    def trainButtonClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | Training Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

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

        self.changeable_frame = Frame(self.admin_page, bg=None)
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

        self.checkDetailButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'
        self.draw_student_detail()

    def draw_student_detail(self):
        self.detail_searchby_frame = Frame(self.changeable_frame, bg='white')
        self.detail_searchby_frame.place(x=5, y=5, width=1190, height=50)

        self.detail_data_frame = Frame(self.changeable_frame, bg='white')
        self.detail_data_frame.place(x=5, y=60, width=1190, height=620)



        ### Btns
        student_add_del_btn = Button(self.detail_searchby_frame, text='Delete', bg='#49a0ae', fg='white',
                                     font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                                     cursor='hand2', command=self.detail_delete_data)
        student_add_del_btn.place(x=30, y=15, width=70, height=22)

        student_add_edit_btn = Button(self.detail_searchby_frame, text='Update', bg='#49a0ae', fg='white',
                                      font=('times new roman', 12), activebackground='#49a0ae',
                                      activeforeground='white',
                                      cursor='hand2', command=self.detail_update_data)
        student_add_edit_btn.place(x=110, y=15, width=70, height=22)




        ### Search


        search = Label(self.detail_searchby_frame, text='Search By :', font=('times new roman', 12), bg='white',
                       fg='black')
        search.place(x=330, y=15)

        stream = Label(self.detail_searchby_frame, text='Stream', font=('Goudy old style', 12, 'bold'), fg='gray',
                       bg='white')
        stream.place(x=440, y=15)

        department = Label(self.detail_searchby_frame, text='Department', font=('Goudy old style', 12, 'bold'),
                           fg='gray',
                           bg='white')
        department.place(x=690, y=15)

        # dictionary

        self.data = {'Engineering': ["Computer", "Electrical", "Chemical", "Mechanical"], 'xyz': ["xyz1", "zyz2"]}
        self.variable_a = StringVar()
        self.variable_b = StringVar()

        self.variable_a.trace('w', self.update_options_B)

        self.optionmenu_a = OptionMenu(self.detail_searchby_frame, self.variable_a, *self.data.keys())
        self.optionmenu_b = OptionMenu(self.detail_searchby_frame, self.variable_b, '')

        self.variable_a.set('Engineering')

        self.optionmenu_a.place(x=510, y=15, width=150, height=25)

        self.optionmenu_b.place(x=800, y=15, width=150, height=25)

        search_btn = Button(self.detail_searchby_frame, text='Search', bg='#49a0ae', fg='white',
                            font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.search)
        search_btn.place(x=1000, y=15, width=60, height=22)


        # Table Frame
        self.student_table_frame = Frame(self.detail_data_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_table_frame.place(x=5, y=5, width=1180, height=610)

        scroll_horizon = Scrollbar(self.student_table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(self.student_table_frame, orient=VERTICAL)
        self.student_data_table = ttk.Treeview(self.student_table_frame,
                                               columns=("enroll_no", "name", "perc", "phno", "email","gender", "dob", "address"),
                                               xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.student_data_table.xview)
        scroll_vertical.config(command=self.student_data_table.yview)
        self.student_data_table.heading("enroll_no", text="EnrollNo.")
        self.student_data_table.column("enroll_no", width=130)
        self.student_data_table.heading("name", text="Student Name")
        self.student_data_table.column("name", width=220)
        self.student_data_table.heading("perc", text="% Attd..")
        self.student_data_table.column("perc", width=50)
        self.student_data_table.heading("phno", text="Phone No.")
        self.student_data_table.column("phno", width=130)
        self.student_data_table.heading("email", text="Email")
        self.student_data_table.column("email", width=160)
        self.student_data_table.heading("gender", text="Gender")
        self.student_data_table.column("gender", width=50)
        self.student_data_table.heading("dob", text="Date Of Birth")
        self.student_data_table.column("dob", width=130)
        self.student_data_table.heading("address", text="Address")
        self.student_data_table.column("address", width=220)
        self.student_data_table['show'] = 'headings'
        self.student_data_table.pack(fill=BOTH, expand=1)

        ##get the selected data from table to fields.
        self.student_data_table.bind('<ButtonRelease-1>', self.get_selection_student_data)

        ##fetch data from student table

        self.fetch_student_data()

    def update_options_B(self, *args):
        countries = self.data[self.variable_a.get()]
        self.variable_b.set(countries[0])
        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))

    def get_selection_student_data(self):
        print("student table")

    def fetch_student_data(self):
        print("access student table")

    def detail_delete_data(self):
        messagebox.askyesno("Confirmation", "Are You Sure ? You want to Delete the Selected data.", parent=self.student_table_frame)

    def detail_update_data(self):
        self.update_page = Toplevel(self.admin_page)
        self.update_page.title("AI-PHACS | Update Detail")
        self.update_page.geometry('385x385+540+250')

        self.edit_detail_frame = Frame(self.update_page, bg=None, )
        self.edit_detail_frame.place(x=5, y=5, width=375, height=375)

        # ### Edit Student
        #
        edit_enroll_no = Label(self.edit_detail_frame, text='EnRoll No. ', font=('Goudy old style', 10, 'bold'),
                               fg='gray',
                               bg=None)
        edit_enroll_no.place(x=50, y=10)
        self.edit_enroll_no_field = Entry(self.edit_detail_frame, font=('times new roman', 10), bg='lightgray')
        self.edit_enroll_no_field.place(x=140, y=13, width=170, height=18)

        edit_student_name = Label(self.edit_detail_frame, text='Name ', font=('Goudy old style', 10, 'bold'),
                                  fg='gray',
                                  bg=None)
        edit_student_name.place(x=50, y=50)
        self.name_field = Entry(self.edit_detail_frame, font=('times new roman', 10), bg='lightgray')
        self.name_field.place(x=140, y=53, width=170, height=18)
        edit_email = Label(self.edit_detail_frame, text='Email', font=('Goudy old style', 10, 'bold'),
                           fg='gray',
                           bg=None)
        edit_email.place(x=50, y=90)
        self.edit_email_field = Entry(self.edit_detail_frame, font=('times new roman', 10), bg='lightgray')
        self.edit_email_field.place(x=140, y=93, width=170, height=18)



        edit_dob = Label(self.edit_detail_frame, text='DOB', font=('Goudy old style', 10, 'bold'),
                         fg='gray',
                         bg=None)
        edit_dob.place(x=50, y=137)

        self.date_field = Entry(self.edit_detail_frame, textvariable=self.dob_date_field_var, font=('times new roman', 10),
                                bg='lightgray')

        self.date_field.place(x=140, y=140, width=30, height=18)

        slash1 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash1.place(x=185, y=137)
        self.month_field = Entry(self.edit_detail_frame, textvariable=self.dob_month_field_var, font=('times new roman', 10),
                                 bg='lightgray')
        self.month_field.place(x=205, y=140, width=30, height=18)
        slash2 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash2.place(x=250, y=137)
        self.year_field = Entry(self.edit_detail_frame, textvariable=self.dob_year_field_var, font=('times new roman', 10),
                                bg='lightgray')
        self.year_field.place(x=270, y=140, width=40, height=18)

        edit_student_gender = Label(self.edit_detail_frame, text='Gender', font=('Goudy old style', 10, 'bold'),
                                    fg='gray',
                                    bg=None)
        edit_student_gender.place(x=50, y=180)
        self.edit_student_gender_combox = ttk.Combobox(self.edit_detail_frame, font=('times new roman', 10),
                                                       state='readonly')
        self.edit_student_gender_combox['values'] = ("M", "F")
        self.edit_student_gender_combox.place(x=140, y=183, width=170, height=18)

        edit_phone_no = Label(self.edit_detail_frame, text='Phone NO.', font=('Goudy old style', 10, 'bold'),
                              fg='gray',
                              bg=None)
        edit_phone_no.place(x=50, y=220)
        self.edit_phone_no_field = Entry(self.edit_detail_frame, font=('times new roman', 10), bg='lightgray')
        self.edit_phone_no_field.place(x=140, y=223, width=170, height=18)

        edit_address = Label(self.edit_detail_frame, text='Address', font=('Goudy old style', 10, 'bold'),
                             fg='gray',
                             bg=None)

        edit_address.place(x=50, y=270)
        edit_address_field = Text(self.edit_detail_frame, width=28, height=3, font=('times new roman', 10),
                                  bg='lightgray')
        edit_address_field.place(x=140, y=263)

        apply_btn = Button(self.edit_detail_frame, text='Update', bg='#49a0ae', fg='white',
                            font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.clear)
        apply_btn.place(x=100, y=330, width=70, height=18)

        cancel_btn = Button(self.edit_detail_frame, text='Cancel', bg='#49a0ae', fg='white',
                                     font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                                     cursor='hand2', command=self.clear)
        cancel_btn.place(x=190, y=330, width=70, height=18)

#### ============================================= USER REGISTRATION  =============================================#####
#### ==============================================================================================================#####


    def addUserClicked(self):
        self.changeable_frame.destroy()

        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | ADD User Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg=None)
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

        self.addUserButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'
        self.draw_add_user()

    def draw_add_user(self):
        self.manage_user_frame = Frame(self.changeable_frame, bg='white')
        self.manage_user_frame.place(x=5, y=5, width=1190, height=130)

        self.user_data_frame = Frame(self.changeable_frame, bg='white')
        self.user_data_frame.place(x=5, y=140, width=1190, height=545)

        ###Variables
        self.user_id_var = StringVar()
        self.user_pass_var = StringVar()
        self.searchby_usertype_var = StringVar()

        sub_banner_title = Label(self.manage_user_frame, text='Manage User', font=('Impact', 30, 'bold'), bg='white',
                                 fg='#49a0ae')
        sub_banner_title.place(relx=0.15, rely=0.5, anchor=CENTER)

        user_id = Label(self.manage_user_frame, text='Set UserName', font=('Goudy old style', 12, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=440, y=15)
        self.id_field = Entry(self.manage_user_frame, textvariable=self.user_id_var, font=('times new roman', 12),
                              bg='lightgray')
        self.id_field.place(x=440, y=50, width=200, height=22)

        password = Label(self.manage_user_frame, text='Set Password', font=('Goudy old style', 12, 'bold'), fg='gray',
                         bg='white')
        password.place(x=675, y=15)
        self.password_field = Entry(self.manage_user_frame, textvariable=self.user_pass_var, font=('times new roman', 12),
                                    bg='lightgray')
        self.password_field.place(x=675, y=50, width=200, height=22)

        user_type = Label(self.manage_user_frame, text='User Type', font=('Goudy old style', 12, 'bold'), fg='gray',
                          bg='white')
        user_type.place(x=910, y=15)
        self.user_type_combox = ttk.Combobox(self.manage_user_frame, font=('times new roman', 12), state='readonly')
        self.user_type_combox['values'] = ("Admin", "Teacher")
        self.user_type_combox.place(x=910, y=50, width=150, height=22)

        # button_frame

        self.btn_frame = Frame(self.manage_user_frame, bg='white', )
        self.btn_frame.place(relwidth=1, y=250, height=50)
        add_btn = Button(self.manage_user_frame, text='Add User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.add_user_submit_clicked)
        add_btn.place(x=490, y=85, width=100, height=30)

        del_btn = Button(self.manage_user_frame, text='Delete User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.delete_data)
        del_btn.place(x=610, y=85, width=100, height=30)

        edit_btn = Button(self.manage_user_frame, text='Update Data', bg='#49a0ae', fg='white',
                          font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                          cursor='hand2', command=self.update_data)
        edit_btn.place(x=730, y=85, width=100, height=30)

        clr_btn = Button(self.manage_user_frame, text='Clear Data', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.clear)
        clr_btn.place(x=850, y=85, width=100, height=30)


        #search_Frame

        self.search_frame = Frame(self.user_data_frame, bg='white', )
        self.search_frame.place(x=510, relwidth=1, y=10, height=50)

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
        table_frame.place(x=5, y=60, width=1180, height=470)

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

        ##fetch data from register table

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