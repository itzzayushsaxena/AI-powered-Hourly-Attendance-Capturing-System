
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.

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

    def close(self):
        self.admin_page.destroy()

    def create_widgets(self):
        self.trainingPhoto = PhotoImage(file="images/Start Training.png", master=self.admin_page)
        self.studentPhoto = PhotoImage(file="images/Add Student.png", master=self.admin_page)
        self.userPhoto = PhotoImage(file="images/Add User.png", master=self.admin_page)
        self.detailPhoto = PhotoImage(file="images/Check Details.png", master=self.admin_page)
        self.attendancePhoto = PhotoImage(file="images/Check Attendancechota.png", master=self.admin_page)
        self.logoutPhoto = PhotoImage(file="images/logout.png", master=self.admin_page)
        # self.exitPhoto  =  PhotoImage(file="images/Exit3.png", master=self.admin_page)
        # self.back = PhotoImage(file="images/back.png")
        #
        # backButton = Button(self.admin_page, image=self.back, command=self.admin_page_backClicked, border=0, height=60,
        #                     width=60, cursor='hand2',)
        # backButton.place(x=20, y=70)

        logout_label = Label(self.admin_page, text='Logout ', font=('Impact', 20, 'bold'), bg=None, fg='gray')
        logout_label.place(x=1100, y=80)
        logoutButton = Button(self.admin_page, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=60,
                              width=60, cursor='hand2', )
        logoutButton.place(x=1200, y=70)

        # banner frame
        banner_frame = Frame(self.admin_page, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Admin Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        btn_frame1 = Frame(self.admin_page)
        btn_frame1.place(relwidth=1, y=140, height=240)
        btn_frame2 = Frame(self.admin_page)
        btn_frame2.place(relwidth=1, y=410, height=240)

        addStudentButton = Button(btn_frame1, image=self.studentPhoto, command=self.addStudentClicked, border=0,
                                  height=190,
                                  width=341, cursor='hand2', )
        addStudentButton.place(relx=0.2, rely=0.55, anchor=CENTER)

        trainButton = Button(btn_frame1, image=self.trainingPhoto, command=self.trainModelClicked, border=0,
                             height=200, width=341, cursor='hand2', )
        trainButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        checkDetailButton = Button(btn_frame1, image=self.detailPhoto, command=self.checkDetailClicked, border=0,
                                   height=190, width=341, cursor='hand2', )
        checkDetailButton.place(relx=0.8, rely=0.5, anchor=CENTER)

        addUserButton = Button(btn_frame2, image=self.userPhoto, command=self.addUserClicked, border=0,
                               height=190, width=341, cursor='hand2', )
        addUserButton.place(relx=0.34, rely=0.5, anchor=CENTER)

        checkAttendanceButton = Button(btn_frame2, image=self.attendancePhoto, command=self.checkAttendanceClicked,
                                       border=0,
                                       height=190, width=341, cursor='hand2', )
        checkAttendanceButton.place(relx=0.65, rely=0.5, anchor=CENTER)

        # exitButton = Button(btn_frame2, image=self.exitPhoto, command=self.exitClicked, border=0,
        #                            height=190, width=341, cursor='hand2',)
        # exitButton.place(relx=0.8, rely=0.5, anchor=CENTER)

    def logoutClicked(self):
        self.admin_page.destroy()
        import main

    # def exitClicked(self):
    #     print("hello")
    #### ============================================= STUDENT REGISTRATION  =============================================##
    #### ==============================================================================================================#####
    # Requirements
    # 1. add student frame
    #     enroll
    #     student name
    #     email
    #     D.O.B
    #     phone-number
    #     address
    #     Images

    #

    def addStudentClicked(self):
        self.admin_page.withdraw()

        self.add_student = Toplevel(self.admin_page)
        self.add_student.title("AI-PHACS | Add Student")
        self.add_student.state('zoomed')
        self.back = PhotoImage(file="images/back.png", master=self.add_student)
        self.add_student.protocol("WM_DELETE_WINDOW", self.close)

        # banner frame
        banner_frame = Frame(self.add_student, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Add Student Page', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        # student entry frame
        self.student_entry_frame = Frame(self.add_student, bd=4, relief=RIDGE, bg='white', )
        self.student_entry_frame.place(x=20, y=80, width=1310, height=640)

        backButton = Button(self.student_entry_frame, image=self.back, command=self.student_backClicked, border=0,
                            height=65,
                            width=65, cursor='hand2', bg='white', activebackground='white')
        # backButton.image = self.back
        backButton.place(x=20, y=20)
        # entry banner frame
        entry_banner_frame = Frame(self.student_entry_frame, bg='#49a0ae', )
        entry_banner_frame.place(x=100, relwidth=1, y=25, height=50)
        entry_banner_title = Label(entry_banner_frame, text='Add New Student', font=('Impact', 30, 'bold'),
                                   bg='#49a0ae',
                                   fg='white')
        entry_banner_title.place(relx=0.48, rely=0.5, anchor=CENTER)
        # student sub_entry1 frame
        self.student_sub_entry1_frame = Frame(self.student_entry_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_sub_entry1_frame.place(x=150, y=130, width=500, height=500)
        # student sub_entry2 frame
        self.student_sub_entry2_frame = Frame(self.student_entry_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_sub_entry2_frame.place(x=650, y=130, width=500, height=500)

        # fields

        enroll_no = Label(self.student_sub_entry1_frame, text='EnRoll No. ', font=('Goudy old style', 15, 'bold'),
                          fg='gray',
                          bg='white')
        enroll_no.place(x=40, y=40)
        self.enroll_no_field = Entry(self.student_sub_entry1_frame, font=('times new roman', 15), bg='lightgray')
        self.enroll_no_field.place(x=190, y=40, width=250, height=30)

        student_name = Label(self.student_sub_entry1_frame, text='Student Name ', font=('Goudy old style', 15, 'bold'),
                             fg='gray',
                             bg='white')
        student_name.place(x=40, y=100)
        self.name_field = Entry(self.student_sub_entry1_frame, font=('times new roman', 15), bg='lightgray')
        self.name_field.place(x=190, y=100, width=250, height=30)

        # #dictionary
        #
        # self.data = {'Engineering': ["Computer", "Electrical", "Chemical", "Mechanical"], 'xyz': ["xyz1", "zyz2"]}
        # self.variable_a = StringVar()
        # self.variable_b = StringVar()
        #
        # self.variable_a.trace('w', self.update_options_B)
        #
        #
        # self.optionmenu_a = OptionMenu(self.student_sub_entry1_frame, self.variable_a, *self.data.keys())
        # self.optionmenu_b = OptionMenu(self.student_sub_entry1_frame, self.variable_b, '')
        #
        # self.variable_a.set('Engineering')
        #
        #
        #
        # stream = Label(self.student_sub_entry1_frame, text='Stream', font=('Goudy old style', 15, 'bold'), fg='gray',
        #                   bg='white')
        # stream.place(x=40, y=80)
        # self.optionmenu_a.place(x=190, y=80, width=250, height=30)
        #
        # department = Label(self.student_sub_entry1_frame, text='Department', font=('Goudy old style', 15, 'bold'), fg='gray',
        #                bg='white')
        # department.place(x=40, y=120)
        # self.optionmenu_b.place(x=190, y=120, width=250, height=30)

        # Year

        # student_year = Label(self.student_sub_entry1_frame, text='Year', font=('Goudy old style', 15, 'bold'),
        #                      fg='gray',
        #                      bg='white')
        # student_year.place(x=40, y=160)
        # self.year_field = Entry(self.student_sub_entry1_frame, font=('times new roman', 15), bg='lightgray')
        # self.year_field.place(x=190, y=160, width=250, height=30)

        email = Label(self.student_sub_entry1_frame, text='Email', font=('Goudy old style', 15, 'bold'),
                      fg='gray',
                      bg='white')
        email.place(x=40, y=160)
        self.email_field = Entry(self.student_sub_entry1_frame, font=('times new roman', 15), bg='lightgray')
        self.email_field.place(x=190, y=160, width=250, height=30)

        dob = Label(self.student_sub_entry1_frame, text='Date Of Birth', font=('Goudy old style', 15, 'bold'),
                    fg='gray',
                    bg='white')
        dob.place(x=40, y=240)
        self.cal = Calendar(self.student_sub_entry1_frame, selectmode='day', year=2020, month=1)
        self.cal.place(x=190, y=220, height=150)

        #     login_btn = Button(self.student_sub_entry1_frame, text='Submit', bg='#d77337', fg='white',
        #                        font=('times new roman', 20), activebackground='#d77337', activeforeground='white',
        #                        cursor='hand2', command=self.cal_output_submit_clicked)
        #     login_btn.place(x=90, y=350, width=100, height=35)
        #
        # def cal_output_submit_clicked(self):
        #     print(self.cal.get_date())
        ## to get --- cal.get_date()--- will give format (month/date/year)

        phone_no = Label(self.student_sub_entry1_frame, text='Phone Number', font=('Goudy old style', 15, 'bold'),
                         fg='gray',
                         bg='white')
        phone_no.place(x=40, y=400)
        self.phone_no_field = Entry(self.student_sub_entry1_frame, font=('times new roman', 15), bg='lightgray')
        self.phone_no_field.place(x=190, y=400, width=250, height=30)

        #     address
        #     Images

        address = Label(self.student_sub_entry2_frame, text='Address', font=('Goudy old style', 15, 'bold'),
                        fg='gray',
                        bg='white')

        address.place(x=40, y=40)
        address_field = Text(self.student_sub_entry2_frame, width=20, height=4, font=('times new roman', 15),
                             bg='lightgray')
        address_field.place(x=190, y=40)

        image = Label(self.student_sub_entry2_frame, text='Upload Image', font=('Goudy old style', 15, 'bold'),
                      fg='gray',
                      bg='white')

        image.place(x=40, y=0)

    # def update_options_B(self, *args):
    #     countries = self.data[self.variable_a.get()]
    #     self.variable_b.set(countries[0])
    #     menu = self.optionmenu_b['menu']
    #     menu.delete(0, 'end')
    #     for country in countries:
    #         menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))

    def student_backClicked(self):

        self.add_student.destroy()
        self.admin_page.deiconify()
        self.admin_page.state('zoomed')

    #### ============================================= TRAIN MODEL  =============================================###########
    #### ==============================================================================================================#####
    # Python program to train model

    def trainModelClicked(self):
        print("heloo")

    #### ============================================= CHECK DETAIL  =============================================##########
    #### ==============================================================================================================#####
    # detail frame
    #     student info with percentage of attendance

    def checkDetailClicked(self):
        self.admin_page.withdraw()
        self.check_detail = Toplevel(self.admin_page)
        self.check_detail.title("AI-PHACS | Student Detail")
        self.check_detail.state('zoomed')
        self.back = PhotoImage(file="images/back.png", master=self.check_detail)
        self.check_detail.protocol("WM_DELETE_WINDOW", self.close)

        # banner frame
        banner_frame = Frame(self.check_detail, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Student Detail Page', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        # student detail frame
        self.student_detail_frame = Frame(self.check_detail, bd=4, relief=RIDGE, bg='white', )
        self.student_detail_frame.place(x=20, y=80, width=1310, height=640)

        backButton = Button(self.student_detail_frame, image=self.back, command=self.student_detail_backClicked,
                            border=0,
                            height=65,
                            width=65, cursor='hand2', bg='white', activebackground='white')

        backButton.place(x=20, y=20)

        # student detail banner frame
        student_detail_banner_frame = Frame(self.student_detail_frame, bg='#49a0ae', )
        student_detail_banner_frame.place(x=100, relwidth=1, y=25, height=50)
        student_detail_title = Label(student_detail_banner_frame, text='Student Detail', font=('Impact', 30, 'bold'),
                                     bg='#49a0ae',
                                     fg='white')
        student_detail_title.place(relx=0.48, rely=0.5, anchor=CENTER)

        ### Edit Student

        edit_enroll_no = Label(self.student_detail_frame, text='EnRoll No. ', font=('Goudy old style', 12, 'bold'),
                               fg='gray',
                               bg='white')
        edit_enroll_no.place(x=40, y=150)
        self.edit_enroll_no_field = Entry(self.student_detail_frame, font=('times new roman', 12), bg='lightgray')
        self.edit_enroll_no_field.place(x=190, y=150, width=160, height=20)

        edit_student_name = Label(self.student_detail_frame, text='Student Name ', font=('Goudy old style', 12, 'bold'),
                                  fg='gray',
                                  bg='white')
        edit_student_name.place(x=40, y=210)
        self.name_field = Entry(self.student_detail_frame, font=('times new roman', 12), bg='lightgray')
        self.name_field.place(x=190, y=210, width=160, height=20)
        edit_email = Label(self.student_detail_frame, text='Email', font=('Goudy old style', 12, 'bold'),
                           fg='gray',
                           bg='white')
        edit_email.place(x=40, y=270)
        self.edit_email_field = Entry(self.student_detail_frame, font=('times new roman', 12), bg='lightgray')
        self.edit_email_field.place(x=190, y=270, width=160, height=20)

        edit_dob = Label(self.student_detail_frame, text='Date Of Birth', font=('Goudy old style', 12, 'bold'),
                         fg='gray',
                         bg='white')
        edit_dob.place(x=40, y=330)
        self.edit_dob_field = Entry(self.student_detail_frame, font=('times new roman', 12), bg='lightgray')
        self.edit_dob_field.place(x=190, y=330, width=160, height=20)

        edit_phone_no = Label(self.student_detail_frame, text='Phone Number', font=('Goudy old style', 12, 'bold'),
                              fg='gray',
                              bg='white')
        edit_phone_no.place(x=40, y=390)
        self.edit_phone_no_field = Entry(self.student_detail_frame, font=('times new roman', 12), bg='lightgray')
        self.edit_phone_no_field.place(x=190, y=390, width=160, height=20)

        edit_address = Label(self.student_detail_frame, text='Address', font=('Goudy old style', 12, 'bold'),
                             fg='gray',
                             bg='white')

        edit_address.place(x=40, y=450)
        edit_address_field = Text(self.student_detail_frame, width=20, height=4, font=('times new roman', 12),
                                  bg='lightgray')
        edit_address_field.place(x=190, y=450)

        # Down_button_frame

        self.student_add_btn_frame = Frame(self.student_detail_frame, bg='white', )
        self.student_add_btn_frame.place(x=30, y=560, width=330, height=50)

        student_add_del_btn = Button(self.student_add_btn_frame, text='Delete Student', bg='#49a0ae', fg='white',
                                     font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                                     cursor='hand2', command=self.delete_data)
        student_add_del_btn.place(x=10, y=10, width=100, height=25)

        student_add_edit_btn = Button(self.student_add_btn_frame, text='Update Student', bg='#49a0ae', fg='white',
                                      font=('times new roman', 12), activebackground='#49a0ae',
                                      activeforeground='white',
                                      cursor='hand2', command=self.update_data)
        student_add_edit_btn.place(x=120, y=10, width=100, height=25)

        student_add_clr_btn = Button(self.student_add_btn_frame, text='Clear Data', bg='#49a0ae', fg='white',
                                     font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                                     cursor='hand2', command=self.clear)
        student_add_clr_btn.place(x=230, y=10, width=100, height=25)

        ### Search

        # filter_label = Label(self.student_detail_frame, text='Filter', font=('Goudy old style', 30, 'bold'),
        #                              bg='white',
        #                              fg='gray')
        # filter_label.place(relx=0.5, rely=0.18, anchor=CENTER)

        search = Label(self.student_detail_frame, text='Search By :', font=('times new roman', 12), bg='white',
                       fg='black')
        search.place(x=500, y=100)

        stream = Label(self.student_detail_frame, text='Stream', font=('Goudy old style', 12, 'bold'), fg='gray',
                       bg='white')
        stream.place(x=630, y=100)

        department = Label(self.student_detail_frame, text='Department', font=('Goudy old style', 12, 'bold'),
                           fg='gray',
                           bg='white')
        department.place(x=890, y=100)

        # dictionary

        self.data = {'Engineering': ["Computer", "Electrical", "Chemical", "Mechanical"], 'xyz': ["xyz1", "zyz2"]}
        self.variable_a = StringVar()
        self.variable_b = StringVar()

        self.variable_a.trace('w', self.update_options_B)

        self.optionmenu_a = OptionMenu(self.student_detail_frame, self.variable_a, *self.data.keys())
        self.optionmenu_b = OptionMenu(self.student_detail_frame, self.variable_b, '')

        self.variable_a.set('Engineering')

        self.optionmenu_a.place(x=700, y=100, width=150, height=25)

        self.optionmenu_b.place(x=1000, y=100, width=150, height=25)

        search_btn = Button(self.student_detail_frame, text='Search', bg='#49a0ae', fg='white',
                            font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.search)
        search_btn.place(x=1180, y=100, width=60, height=25)

        # Table Frame
        self.student_table_frame = Frame(self.student_detail_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_table_frame.place(x=400, y=130, width=900, height=500)

        scroll_horizon = Scrollbar(self.student_table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(self.student_table_frame, orient=VERTICAL)
        self.student_data_table = ttk.Treeview(self.student_table_frame,
                                               columns=("enroll_no", "name", "perc", "phno", "email", "dob", "address"),
                                               xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.student_data_table.xview)
        scroll_vertical.config(command=self.student_data_table.yview)
        self.student_data_table.heading("enroll_no", text="EnrollNo.")
        self.student_data_table.column("enroll_no", width=90)
        self.student_data_table.heading("name", text="Student Name")
        self.student_data_table.column("name", width=250)
        self.student_data_table.heading("perc", text="Attendance Percentage")
        self.student_data_table.column("perc", width=150)
        self.student_data_table.heading("phno", text="Phone No.")
        self.student_data_table.heading("email", text="Email")
        self.student_data_table.heading("dob", text="Date Of Birth")
        self.student_data_table.heading("address", text="Address")
        self.student_data_table['show'] = 'headings'
        self.student_data_table.pack(fill=BOTH, expand=1)

    def update_options_B(self, *args):
        countries = self.data[self.variable_a.get()]
        self.variable_b.set(countries[0])
        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.variable_b.set(nation))

    def student_detail_backClicked(self):

        self.check_detail.destroy()
        self.admin_page.deiconify()
        self.admin_page.state('zoomed')

    #### ============================================= CHECK ATTENDANCE  =============================================######
    #### ==============================================================================================================#####
    # attendance frame
    #      attendance table with full daily info & percentage

    def checkAttendanceClicked(self):
        self.admin_page.withdraw()
        self.check_attendance = Toplevel(self.admin_page)
        self.check_attendance.title("AI-PHACS | Student Attendance Page")
        self.check_attendance.state('zoomed')
        self.attendance_back = PhotoImage(file="images/back.png", master=self.check_attendance)
        self.check_attendance.protocol("WM_DELETE_WINDOW", self.close)

        # banner frame
        banner_frame = Frame(self.check_attendance, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Student Attendance Page', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)
        # student Attendance frame
        self.student_attendance_frame = Frame(self.check_attendance, bd=4, relief=RIDGE, bg='white', )
        self.student_attendance_frame.place(x=20, y=80, width=1310, height=640)

        backButton = Button(self.student_attendance_frame, image=self.attendance_back,
                            command=self.student_attendance_backClicked,
                            border=0,
                            height=65,
                            width=65, cursor='hand2', bg='white', activebackground='white')

        backButton.place(x=20, y=20)

        # student attendance banner frame
        student_attendance_banner_frame = Frame(self.student_attendance_frame, bg='#49a0ae', )
        student_attendance_banner_frame.place(x=100, relwidth=1, y=25, height=50)
        student_attendance_title = Label(student_attendance_banner_frame, text='Student Attendance',
                                         font=('Impact', 30, 'bold'),
                                         bg='#49a0ae',
                                         fg='white')
        student_attendance_title.place(relx=0.48, rely=0.5, anchor=CENTER)

        # search
        attendance_search = Label(self.student_attendance_frame, text='Search By : ', font=('times new roman', 12),
                                  bg='white',
                                  fg='black')
        attendance_search.place(x=100, y=100)
        enroll_no = Label(self.student_attendance_frame, text='Enroll No. ', font=('Goudy old style', 12), fg='gray',
                          bg='white')
        enroll_no.place(x=185, y=100)
        self.enroll_field = Entry(self.student_attendance_frame, font=('times new roman', 12),
                                  bg='lightgray')
        self.enroll_field.place(x=255, y=100, width=120, height=25)
        attendance_search_btn = Button(self.student_attendance_frame, text='Search', bg='#49a0ae', fg='white',
                                       font=('times new roman', 12), activebackground='#49a0ae',
                                       activeforeground='white',
                                       cursor='hand2', command=self.search)
        attendance_search_btn.place(x=390, y=100, width=60, height=25)
        # edit
        edit = Label(self.student_attendance_frame, text='Edit', font=('times new roman', 12), bg='white',
                     fg='black')
        edit.place(x=500, y=100)

        edit_btn = Button(self.student_attendance_frame, text='Edit', bg='#49a0ae', fg='white',
                          font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                          cursor='hand2', command=self.search)
        edit_btn.place(x=1180, y=100, width=60, height=25)

        # Table Frame
        self.student_info_table_frame = Frame(self.student_attendance_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_info_table_frame.place(x=5, y=140, width=795, height=490)

        scroll_horizon = Scrollbar(self.student_info_table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(self.student_info_table_frame, orient=VERTICAL)
        self.student_info_data_table = ttk.Treeview(self.student_info_table_frame,
                                                    columns=("enroll_no", "name", "perc"),
                                                    xscrollcommand=scroll_horizon.set,
                                                    yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.student_info_data_table.xview)
        scroll_vertical.config(command=self.student_info_data_table.yview)
        self.student_info_data_table.heading("enroll_no", text="EnrollNo.")
        self.student_info_data_table.column("enroll_no", width=140)
        self.student_info_data_table.heading("name", text="Student Name")
        self.student_info_data_table.column("name", width=250)
        self.student_info_data_table.heading("perc", text="Attendance Percentage")
        self.student_info_data_table.column("perc", width=40)

        self.student_info_data_table['show'] = 'headings'
        self.student_info_data_table.pack(fill=BOTH, expand=1)

        # attendance Table Frame
        self.student_attendance_table_frame = Frame(self.student_attendance_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_attendance_table_frame.place(x=800, y=140, width=500, height=490)

        scroll_horizon = Scrollbar(self.student_attendance_table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(self.student_attendance_table_frame, orient=VERTICAL)
        self.student_attendance_data_table = ttk.Treeview(self.student_attendance_table_frame,
                                                          columns=("date", "p/a"),
                                                          xscrollcommand=scroll_horizon.set,
                                                          yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.student_attendance_data_table.xview)
        scroll_vertical.config(command=self.student_attendance_data_table.yview)
        self.student_attendance_data_table.heading("date", text="Date")
        self.student_attendance_data_table.column("date", width=140)
        self.student_attendance_data_table.heading("p/a", text="Present / Absent")
        self.student_attendance_data_table.column("p/a", width=250)

        self.student_attendance_data_table['show'] = 'headings'
        self.student_attendance_data_table.pack(fill=BOTH, expand=1)

    def student_attendance_backClicked(self):
        self.check_attendance.destroy()
        self.admin_page.deiconify()
        self.admin_page.state('zoomed')

    #### ============================================= USER REGISTRATION  =============================================#####
    #### ==============================================================================================================#####

    def addUserClicked(self):
        self.admin_page.withdraw()
        self.add_user = Toplevel(self.admin_page)
        self.add_user.title("AI-PHACS | User Registration")
        self.add_user.state('zoomed')
        self.back = PhotoImage(file="images/back.png", master=self.add_user)
        self.add_user.protocol("WM_DELETE_WINDOW", self.close)

        ###Variables
        self.user_id_var = StringVar()
        self.user_pass_var = StringVar()
        self.searchby_usertype_var = StringVar()

        # banner frame
        banner_frame = Frame(self.add_user, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Manage User Page', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        # entry frame
        self.entry_frame = Frame(self.add_user, bg='white', )
        self.entry_frame.place(x=20, y=80, width=550, height=450)

        backButton = Button(self.entry_frame, image=self.back, command=self.add_user_backClicked, border=0, height=65,
                            width=65, cursor='hand2', bg='white', activebackground='white')
        # backButton.image = self.back
        backButton.place(x=20, y=20)

        sub_banner_frame = Frame(self.entry_frame, bg='#49a0ae', )
        sub_banner_frame.place(x=120, relwidth=1, y=26, height=50)
        sub_banner_title = Label(sub_banner_frame, text='Manage User', font=('Impact', 30, 'bold'), bg='#49a0ae',
                                 fg='white')
        sub_banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        user_id = Label(self.entry_frame, text='Set UserName', font=('Goudy old style', 15, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=90, y=140)
        self.id_field = Entry(self.entry_frame, textvariable=self.user_id_var, font=('times new roman', 15),
                              bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)

        password = Label(self.entry_frame, text='Set Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                         bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(self.entry_frame, textvariable=self.user_pass_var, font=('times new roman', 15),
                                    bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        user_type = Label(self.entry_frame, text='User Type', font=('Goudy old style', 15, 'bold'), fg='gray',
                          bg='white')
        user_type.place(x=90, y=280)
        self.user_type_combox = ttk.Combobox(self.entry_frame, font=('times new roman', 15), state='readonly')
        self.user_type_combox['values'] = ("Admin", "Teacher")
        self.user_type_combox.place(x=90, y=310, width=200, height=35)

        # button_frame

        self.btn_frame = Frame(self.entry_frame, bg='white', )
        self.btn_frame.place(relwidth=1, y=390, height=50)
        add_btn = Button(self.btn_frame, text='Add User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.add_user_submit_clicked)
        add_btn.place(x=40, y=10, width=100, height=35)

        del_btn = Button(self.btn_frame, text='Delete User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.delete_data)
        del_btn.place(x=160, y=10, width=100, height=35)

        edit_btn = Button(self.btn_frame, text='Update Data', bg='#49a0ae', fg='white',
                          font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                          cursor='hand2', command=self.update_data)
        edit_btn.place(x=280, y=10, width=100, height=35)

        clr_btn = Button(self.btn_frame, text='Clear Data', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.clear)
        clr_btn.place(x=400, y=10, width=100, height=35)

        # data frame

        self.data_frame = Frame(self.add_user, bg='white', )
        self.data_frame.place(x=590, y=80, width=750, height=650)

        data_banner_frame = Frame(self.data_frame, bg='#49a0ae', )
        data_banner_frame.place(relwidth=1, y=26, height=50)
        data_banner_title = Label(data_banner_frame, text='User Data', font=('Impact', 30, 'bold'), bg='#49a0ae',
                                  fg='white')
        data_banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        search = Label(self.data_frame, text='Search By :', font=('times new roman', 20), bg='white',
                       fg='black')
        search.place(x=30, y=96)

        user_type = Label(self.data_frame, text='User Type', font=('Goudy old style', 17), fg='gray',
                          bg='white')
        user_type.place(x=170, y=96)
        self.search_user_type_combox = ttk.Combobox(self.data_frame, textvariable=self.searchby_usertype_var,
                                                    font=('times new roman', 15), state='readonly')
        self.search_user_type_combox['values'] = ("Admin", "Teacher")
        self.search_user_type_combox.place(x=280, y=96, width=100, height=30, )

        search_btn = Button(self.data_frame, text='Search', bg='#49a0ae', fg='white',
                            font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.search)
        search_btn.place(x=400, y=96, width=60, height=35)

        show_all_btn = Button(self.data_frame, text='Show All', bg='#49a0ae', fg='white',
                              font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                              cursor='hand2', command=self.fetch_data)
        show_all_btn.place(x=490, y=96, width=60, height=35)

        # Table Frame
        table_frame = Frame(self.data_frame, bd=4, relief=RIDGE, bg='white')
        table_frame.place(x=15, y=150, width=720, height=480)

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
            messagebox.showerror("Error", "All field Are Required To Add User", parent=self.entry_frame)
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
            messagebox.showerror("Error", "Select User From Table To Update", parent=self.entry_frame)
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
            messagebox.showerror("Error", "Select User From Table To Delete", parent=self.entry_frame)
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

    def add_user_backClicked(self):
        self.clear()
        self.add_user.destroy()
        self.admin_page.deiconify()
        self.admin_page.state('zoomed')


root = Tk()
obj = Admin_Page(root)
root.mainloop()