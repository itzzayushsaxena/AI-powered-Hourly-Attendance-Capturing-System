import os
from tkinter import *
from tkinter import ttk

from tkinter import messagebox
import pymysql
import datetime
import re
from cryptography.fernet import Fernet

class Admin_Page:
    def __init__(self, root):
        self.admin_page = root
        self.admin_page.title("AI-PHACS | Admin Page")
        self.admin_page.state('zoomed')
        self.create_widgets()

    def connect_database(self):
        self.con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
        self.cursor = self.con.cursor()

    def create_widgets(self):

        self.trainingPhoto = PhotoImage(file="images/Start Training Final.png", master=self.admin_page)
        self.timetablePhoto = PhotoImage(file="images/Add Timetable Final.png", master=self.admin_page)
        self.studentPhoto = PhotoImage(file="images/Add Student Final.png", master=self.admin_page)
        self.userPhoto = PhotoImage(file="images/Add User Final.png", master=self.admin_page)
        self.detailPhoto = PhotoImage(file="images/Check Details Final.png", master=self.admin_page)
        self.attendancePhoto = PhotoImage(file="images/Check Attendance5.png", master=self.admin_page)
        self.logoutPhoto = PhotoImage(file="images/logout4.png", master=self.admin_page)

        # banner frame
        self.banner_frame = Frame(self.admin_page, bg='#49a0ae', )
        self.banner_frame.place(x=155, relwidth=1, y=0, height=50)
        self.banner_title = Label(self.banner_frame, text='Admin | Add Student Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        with open('session_id.txt', 'r') as f:
            lines = f.readlines()
            key = lines[0].strip()
            encrpted_text = lines[1].strip()
        fer = Fernet(key.encode())
        session_id = (fer.decrypt(encrpted_text.encode())).decode("utf-8")
        self.connect_database()
        self.cursor.execute("select username from register where reg_id=%s", session_id)
        row_name = self.cursor.fetchall()
        self.user_logged_in_var = StringVar()
        if (len(row_name) != 0):
            self.user_logged_in_var.set(row_name[0][0])

        logout_label = Label(self.banner_frame, text="Welcome,  ", font=('times new roman', 10, 'bold'),
                             bg='#49a0ae',
                             fg='white')
        logout_label.place(x=970, y=1)
        logout_label = Label(self.banner_frame, textvariable=self.user_logged_in_var, font=('times new roman', 15, 'bold'), bg='#49a0ae',
                             fg='white')
        logout_label.place(x=990, y=19)

        logoutButton = Button(self.banner_frame, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=45,
                              width=45, cursor='hand2', bg='#49a0ae', activebackground='#49a0ae', )
        logoutButton.place(x=1150, y=5)

        ###### FRAMES

        self.btn_frame = Frame(self.admin_page, bg=None)
        self.btn_frame.place(x=5, relheight=1, width=150)

        self.changeable_frame = Frame(self.admin_page, bg='white')
        self.changeable_frame.place(x=310, y=55, height=680, width=1050)

        self.admin_template()

    def admin_template(self):

        scroll_vertical = Scrollbar(self.btn_frame, orient=VERTICAL)
        scroll_vertical.pack(side=RIGHT, fill=Y, expand=FALSE)

        canvas = Canvas(self.btn_frame, bd=0, highlightthickness=0,
                        yscrollcommand=scroll_vertical.set, width=400, height=800)

        canvas.pack(padx=8, pady=5, side=LEFT, fill=Y, expand=TRUE)
        scroll_vertical.config(command=canvas.yview)

        # reset the view
        canvas.yview_moveto(0)

        def _bound_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)

        def _unbound_to_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        interior = Frame(canvas)

        interior.bind('<Enter>', _bound_to_mousewheel)
        interior.bind('<Leave>', _unbound_to_mousewheel)

        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        self.checkAttendanceButton = Button(interior, image=self.attendancePhoto,
                                            command=self.checkAttendanceClicked,
                                            border=0,
                                            height=120, width=120, cursor='hand2', )
        self.checkAttendanceButton.pack(padx=0, pady=5, side=TOP)

        self.addUserButton = Button(interior, image=self.userPhoto, command=self.addUserClicked, border=0,
                                    height=120, width=120, cursor='hand2', )
        self.addUserButton.pack(padx=0, pady=5, side=TOP)

        self.addStudentButton = Button(interior, image=self.studentPhoto, command=self.draw_add_student, border=0,
                                       height=120,
                                       width=120, cursor='hand2', state='disable', )
        self.addStudentButton.pack(padx=0, pady=5, side=TOP)

        self.trainButton = Button(interior, image=self.trainingPhoto, command=self.trainButtonClicked, border=0,
                                  height=120, width=120, cursor='hand2', )
        self.trainButton.pack(padx=0, pady=5, side=TOP)

        self.checkDetailButton = Button(interior, image=self.detailPhoto, command=self.checkDetailClicked,
                                        border=0,
                                        height=120, width=120, cursor='hand2', )
        self.checkDetailButton.pack(padx=0, pady=5, side=TOP)


        self.addTimeTableButton = Button(interior, image=self.timetablePhoto, command=self.addTimeTableClicked,
                                         border=0,
                                         height=120, width=120, cursor='hand2', )
        self.addTimeTableButton.pack(padx=0, pady=5, side=TOP)

        self.trainButton['state'] = 'normal'
        self.addTimeTableButton['state'] = 'normal'
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
        self.changeable_frame.place(x=165, y=60, height=675, width=1190)

        self.addStudentButton['state'] = 'disable'
        self.addTimeTableButton['state'] = 'normal'
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
        self.phone_no_var = StringVar()

        self.add_student_frame = Frame(self.changeable_frame, bg='white', bd=4, relief=RIDGE)
        self.add_student_frame.place(x=5, y=5, height=665, width=1185)
        self.upload_Photo = PhotoImage(file="images/Profile_400px.png", master=self.add_student_frame)

        student_name = Label(self.add_student_frame, text='Student Name ', font=('Goudy old style', 15, 'bold'),
                             fg='gray',
                             bg='white')
        student_name.place(x=135, y=60)
        self.name_field = Entry(self.add_student_frame, textvariable=self.student_name_var,
                                font=('times new roman', 15), bg='lightgray')
        self.name_field.place(x=305, y=60, width=250, height=30)

        enroll_no = Label(self.add_student_frame, text='EnRoll No. ', font=('Goudy old style', 15, 'bold'),
                          fg='gray',
                          bg='white')
        enroll_no.place(x=135, y=120)
        self.enroll_no_field = Entry(self.add_student_frame, textvariable=self.enroll_no_var,
                                     font=('times new roman', 15), bg='lightgray')
        self.enroll_no_field.place(x=305, y=120, width=250, height=30)

        email = Label(self.add_student_frame, text='Email', font=('Goudy old style', 15, 'bold'),
                      fg='gray',
                      bg='white')
        email.place(x=135, y=200)
        self.email_field = Entry(self.add_student_frame, textvariable=self.student_email_var,
                                 font=('times new roman', 15), bg='lightgray')
        self.email_field.place(x=305, y=200, width=250, height=30)

        dob = Label(self.add_student_frame, text='Date Of Birth', font=('Goudy old style', 15, 'bold'),
                    fg='gray',
                    bg='white')
        dob.place(x=135, y=280)

        self.date_field = Entry(self.add_student_frame, textvariable=self.dob_date_field_var,
                                font=('times new roman', 15), bg='lightgray')

        self.date_field.place(x=305, y=280, width=50, height=30)

        slash1 = Label(self.add_student_frame, text='/', font=('Goudy old style', 20), bg='white', fg='gray')
        slash1.place(x=365, y=276)
        self.month_field = Entry(self.add_student_frame, textvariable=self.dob_month_field_var,
                                 font=('times new roman', 15), bg='lightgray')
        self.month_field.place(x=385, y=280, width=50, height=30)
        slash2 = Label(self.add_student_frame, text='/', font=('Goudy old style', 20), bg='white', fg='gray')
        slash2.place(x=445, y=276)
        self.year_field = Entry(self.add_student_frame, textvariable=self.dob_year_field_var,
                                font=('times new roman', 15), bg='lightgray')
        self.year_field.place(x=465, y=280, width=90, height=30)
        self.date_field.bind('<ButtonRelease-1>', self.date_selected)
        self.month_field.bind('<ButtonRelease-1>', self.month_selected)
        self.year_field.bind('<ButtonRelease-1>', self.year_selected)

        student_gender = Label(self.add_student_frame, text='Gender', font=('Goudy old style', 15, 'bold'), fg='gray',
                               bg='white')
        student_gender.place(x=135, y=360)
        self.student_gender_combox = ttk.Combobox(self.add_student_frame, font=('times new roman', 15),
                                                  state='readonly')
        self.student_gender_combox['values'] = ("M", "F")
        self.student_gender_combox.place(x=305, y=360, width=250, height=30)

        phone_no = Label(self.add_student_frame, text='Phone Number', font=('Goudy old style', 15, 'bold'),
                         fg='gray',
                         bg='white')
        phone_no.place(x=135, y=420)
        self.phone_no_field = Entry(self.add_student_frame, textvariable=self.phone_no_var,
                                    font=('times new roman', 15), bg='lightgray')
        self.phone_no_field.place(x=305, y=420, width=250, height=30)

        address = Label(self.add_student_frame, text='Address', font=('Goudy old style', 15, 'bold'),
                        fg='gray',
                        bg='white')

        address.place(x=135, y=480)
        self.address_field = Text(self.add_student_frame, width=25, height=3, font=('times new roman', 15),
                                  bg='lightgray')
        self.address_field.place(x=305, y=480)

        self.upload_image_frame = Frame(self.add_student_frame, )
        self.upload_image_frame.place(x=700, y=110, height=360, width=320, )
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
                                        font=('times new roman', 14, 'bold'), activebackground='#49a0ae',
                                        activeforeground='white',
                                        cursor='hand2', command=self.add_student_submit_clicked)
        add_student_submit_btn.place(x=495, y=575)

    def date_selected(self, event):
        self.dob_date_field_var.set('')

    def month_selected(self, event):
        self.dob_month_field_var.set('')

    def year_selected(self, event):
        self.dob_year_field_var.set('')

    def add_student_submit_clicked(self):
        print("Adding NewStudent.....")
        print("Checking validations.....")
        if self.validate_all_fields():
            print(self.validate_number_field())
            if self.validate_number_field():
                print(self.is_valid_email())
                if self.is_valid_email():
                    print("Validation Check Done.....")
                    print("Connecting Database.....")
                    self.connect_database()
                    print("Database Connected sucessfully")
                    if self.cursor.execute("select enroll_no from student where enroll_no=%s",
                                           self.enroll_no_field.get()):
                        print("Student with Same enrollnment number exist.....")
                        messagebox.showerror("Error",
                                             "Student With Same Enrollnment No. Exist, Try Different Enrollnment No.")
                    else:

                        self.cursor.execute(
                            "insert into student(enroll_no,name,email,dob,gender,phone_no,address,depart_id)"
                            "values(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.enroll_no_field.get(),
                                self.name_field.get(),
                                self.email_field.get(),
                                str(self.year_field.get()) + "/" + str(self.month_field.get()) + "/" + str(
                                    self.date_field.get()),
                                self.student_gender_combox.get(),
                                self.phone_no_field.get(),
                                self.address_field.get('1.0', END),
                                (self.enroll_no_field.get()[7] + self.enroll_no_field.get()[8])
                            ))

                        self.con.commit()
                        print("newStudent Added Sucessfully.....")
                        self.add_student_clear()
                        self.con.close()
                        messagebox.showinfo("sucess", "Data Added Sucessfully.")
        else:
            print("validation of allFields Fails")

    def validate_all_fields(self):
        # print(self.address_field.get('1.0', END) == '')
        if self.name_field.get() == '':
            messagebox.showerror("Error", "Please enter full name to proceed", parent=self.add_student_frame)

        elif self.enroll_no_field.get() == '':
            messagebox.showerror("Error", "Please enter Enrollnment No. to proceed", parent=self.add_student_frame)

        elif self.email_field.get() == '':
            messagebox.showerror("Error", "Please enter Email to proceed", parent=self.add_student_frame)

        elif self.student_gender_combox.get() == '':
            messagebox.showerror("Error", "Please Select Your Gender to proceed", parent=self.add_student_frame)

        elif (self.dob_date_field_var.get() == '' or self.dob_month_field_var.get() == ''
              or self.dob_year_field_var.get() == ''):
            messagebox.showerror("Error", "Please enter Date Of Birth to proceed", parent=self.add_student_frame)

        elif self.phone_no_field.get() == '':
            messagebox.showerror("Error", "Please enter Phone No. to proceed", parent=self.add_student_frame)

        elif self.address_field.get('1.0', END) == '':
            messagebox.showerror("Error", "Please enter Address to proceed", parent=self.add_student_frame)

        else:
            return True

    def validate_number_field(self):

        if ((self.enroll_no_field.get().isdigit()) and (len(self.enroll_no_field.get()) == 12)):
            if ((self.phone_no_field.get().isdigit())) and (len(self.phone_no_field.get()) == 10):
                if ((self.date_field.get().isdigit()) and (self.month_field.get().isdigit())
                        and (self.year_field.get().isdigit()) and (len(self.date_field.get()) == 2)
                        and (len(self.month_field.get()) == 2) and (len(self.year_field.get()) == 4)):
                    return True
                else:
                    messagebox.showerror("Error", "Please enter Date According To Format to proceed",
                                         parent=self.add_student_frame)

            else:
                messagebox.showerror("Error", "Please enter 10 digit Phone No. to proceed",
                                     parent=self.add_student_frame)

        else:
            messagebox.showerror("Error", "Please enter 12 digit Enrollnment No. to proceed",
                                 parent=self.add_student_frame)

    def is_valid_email(self):
        if len(self.email_field.get()) > 10:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                        self.email_field.get()) is not None:
                return True
            else:
                messagebox.showerror("Error", "Please enter valid Email id to proceed", parent=self.add_student_frame)
                return False

    def add_student_clear(self):
        self.student_name_var.set('')
        self.enroll_no_var.set('')
        self.student_email_var.set('')
        self.dob_date_field_var.set('DD')
        self.dob_month_field_var.set('MM')
        self.dob_year_field_var.set('YYYY')
        self.student_gender_combox.set('')
        self.phone_no_var.set('')
        self.address_field.delete('1.0', END)

    #### ============================================= Training           =============================================#####
    #### ==============================================================================================================#####
    def trainButtonClicked(self):
        # os.system('train.py')
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | Training Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

        self.trainButton['state'] = 'disable'
        self.addTimeTableButton['state'] = 'normal'
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
        self.addTimeTableButton['state'] = 'normal'
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
        student_add_edit_btn.place(x=120, y=15, width=70, height=22)

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

        self.data = {'Engineering': ["Computer", "Electrical", "Chemical", "Civil", "Mechanical"],
                     'xyz': ["xyz1", "zyz2"]}
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
                            cursor='hand2', command=self.search_detail)
        search_btn.place(x=1000, y=15, width=60, height=22)

        search_all_btn = Button(self.detail_searchby_frame, text='Show All', bg='#49a0ae', fg='white',
                                font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                                cursor='hand2', command=self.fetch_student_data)
        search_all_btn.place(x=1080, y=15, width=60, height=22)

        # Count row
        count_row_label = Label(self.detail_data_frame, text='No. Of Student  :  ',
                                font=('Goudy old style', 12, 'bold'),
                                fg='gray',
                                bg='white')
        count_row_label.place(x=30, y=5)
        self.count_student_row = Label(self.detail_data_frame, text='', font=('Goudy old style', 12, 'bold'),
                                       fg='gray',
                                       bg='white')
        self.count_student_row.place(x=170, y=5)

        # Show Department
        department_label = Label(self.detail_data_frame, text='Department  :  ',
                                 font=('Goudy old style', 12, 'bold'),
                                 fg='gray',
                                 bg='white')
        department_label.place(x=220, y=5)
        self.show_department = Label(self.detail_data_frame, text='All', font=('Goudy old style', 12, 'bold'),
                                     fg='gray',
                                     bg='white')
        self.show_department.place(x=330, y=5)

        # Table Frame
        self.student_table_frame = Frame(self.detail_data_frame, bd=4, relief=RIDGE, bg='white', )
        self.student_table_frame.place(x=5, y=25, width=1180, height=590)

        scroll_horizon = Scrollbar(self.student_table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(self.student_table_frame, orient=VERTICAL)
        self.student_data_table = ttk.Treeview(self.student_table_frame,
                                               columns=(
                                               "srno", "enroll_no", "name", "perc", "phno", "email", "gender", "dob",
                                               "address"),
                                               xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.student_data_table.xview)
        scroll_vertical.config(command=self.student_data_table.yview)
        self.student_data_table.heading("srno", text="SrNo.")
        self.student_data_table.column("srno", width=50)
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

    def get_selection_student_data(self, event):
        selection_row = self.student_data_table.focus()
        contents = self.student_data_table.item(selection_row)
        self.student_detail_row = contents['values']
        # print(self.student_detail_row)

    def fetch_student_data(self):
        try:
            self.connect_database()
            self.show_department.config(text='All')
            self.cursor.execute("select * from student")
            rows = self.cursor.fetchall()
            self.count_student_row.config(text=len(rows))
            if len(rows) != 0:
                self.student_data_table.delete(*self.student_data_table.get_children())
                count = 1
                for row in rows:
                    # print(row)
                    self.student_data_table.insert('', END, values=(
                    count, row[0], row[1], 0, row[5], row[2], row[4], row[3], row[6]))
                    self.con.commit()
                    count += 1
            self.con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")

    def detail_delete_data(self):
        if hasattr(self, 'student_detail_row'):
            m = messagebox.askyesno("Confirmation", "Are You Sure ? You want to Delete the Selected data.",
                                    parent=self.student_table_frame)
            # print(m)
            if m:
                try:
                    self.connect_database()
                    self.cursor.execute("delete from student where enroll_no=%s", self.student_detail_row[1])
                    self.con.commit()
                    self.con.close()
                    messagebox.showinfo("Success", "Student is Delete succesfully.")
                    self.fetch_student_data()

                except Exception as ex:
                    messagebox.showerror("Error",
                                         f"Action Failed Due To : {str(ex)}")
        else:
            messagebox.showerror("Error", "Select student From Table To Delete")
            return

    def detail_update_data(self):

        if hasattr(self, 'student_detail_row'):
            self.update_page = Toplevel(self.admin_page)
            self.update_page.title("AI-PHACS | Update Detail")
            self.update_page.geometry('385x385+540+250')

            self.edit_detail_frame = Frame(self.update_page, bg=None, )
            self.edit_detail_frame.place(x=5, y=5, width=375, height=375)

            ## Variable

            self.edit_enroll_var = StringVar()
            self.edit_enroll_var.set(self.student_detail_row[1])
            self.edit_name_var = StringVar()
            self.edit_name_var.set(self.student_detail_row[2])
            self.edit_email_var = StringVar()
            self.edit_email_var.set(self.student_detail_row[5])
            # print(datetime.datetime.strptime(self.student_detail_row[6], "%Y-%m-%d"))
            edit_dob = datetime.datetime.strptime(self.student_detail_row[7], "%Y-%m-%d")
            # print(format(edit_dob.month,'02'))
            # print(format(edit_dob.day, '02'))
            self.edit_date_var = StringVar()
            self.edit_date_var.set(format(edit_dob.day, '02'))
            self.edit_month_var = StringVar()
            self.edit_month_var.set(format(edit_dob.month, '02'))
            self.edit_year_var = StringVar()
            self.edit_year_var.set(edit_dob.year)
            self.edit_gender_var = StringVar()
            self.edit_gender_var.set(self.student_detail_row[6])
            self.edit_phone_no_var = StringVar()
            self.edit_phone_no_var.set(self.student_detail_row[4])
        else:
            messagebox.showerror("Error", "Select student From Table To Update")
            return
        # ### Edit Student
        #
        edit_enroll_no = Label(self.edit_detail_frame, text='EnRoll No. ', font=('Goudy old style', 10, 'bold'),
                               fg='gray',
                               bg=None)
        edit_enroll_no.place(x=50, y=10)
        self.edit_enroll_no_field = Entry(self.edit_detail_frame, textvariable=self.edit_enroll_var,
                                          font=('times new roman', 10), bg='lightgray')
        self.edit_enroll_no_field.place(x=140, y=13, width=170, height=18)

        edit_student_name = Label(self.edit_detail_frame, text='Name ', font=('Goudy old style', 10, 'bold'),
                                  fg='gray',
                                  bg=None)
        edit_student_name.place(x=50, y=50)
        self.edit_name_field = Entry(self.edit_detail_frame, textvariable=self.edit_name_var,
                                     font=('times new roman', 10), bg='lightgray')
        self.edit_name_field.place(x=140, y=53, width=170, height=18)
        edit_email = Label(self.edit_detail_frame, text='Email', font=('Goudy old style', 10, 'bold'),
                           fg='gray',
                           bg=None)
        edit_email.place(x=50, y=90)
        self.edit_email_field = Entry(self.edit_detail_frame, textvariable=self.edit_email_var,
                                      font=('times new roman', 10), bg='lightgray')
        self.edit_email_field.place(x=140, y=93, width=170, height=18)

        edit_dob = Label(self.edit_detail_frame, text='DOB', font=('Goudy old style', 10, 'bold'),
                         fg='gray',
                         bg=None)
        edit_dob.place(x=50, y=137)

        self.edit_date_field = Entry(self.edit_detail_frame, textvariable=self.edit_date_var,
                                     font=('times new roman', 10),
                                     bg='lightgray')

        self.edit_date_field.place(x=140, y=140, width=30, height=18)

        slash1 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash1.place(x=185, y=137)
        self.edit_month_field = Entry(self.edit_detail_frame, textvariable=self.edit_month_var,
                                      font=('times new roman', 10),
                                      bg='lightgray')
        self.edit_month_field.place(x=205, y=140, width=30, height=18)
        slash2 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash2.place(x=250, y=137)
        self.edit_year_field = Entry(self.edit_detail_frame, textvariable=self.edit_year_var,
                                     font=('times new roman', 10),
                                     bg='lightgray')
        self.edit_year_field.place(x=270, y=140, width=40, height=18)

        edit_student_gender = Label(self.edit_detail_frame, text='Gender', font=('Goudy old style', 10, 'bold'),
                                    fg='gray',
                                    bg=None)
        edit_student_gender.place(x=50, y=180)
        self.edit_student_gender_combox = ttk.Combobox(self.edit_detail_frame, textvariable=self.edit_gender_var,
                                                       font=('times new roman', 10),
                                                       state='readonly')
        self.edit_student_gender_combox['values'] = ("M", "F")
        self.edit_student_gender_combox.place(x=140, y=183, width=170, height=18)

        edit_phone_no = Label(self.edit_detail_frame, text='Phone NO.', font=('Goudy old style', 10, 'bold'),
                              fg='gray',
                              bg=None)
        edit_phone_no.place(x=50, y=220)
        self.edit_phone_no_field = Entry(self.edit_detail_frame, textvariable=self.edit_phone_no_var,
                                         font=('times new roman', 10), bg='lightgray')
        self.edit_phone_no_field.place(x=140, y=223, width=170, height=18)

        edit_address = Label(self.edit_detail_frame, text='Address', font=('Goudy old style', 10, 'bold'),
                             fg='gray',
                             bg=None)

        edit_address.place(x=50, y=270)
        self.edit_address_field = Text(self.edit_detail_frame, width=28, height=3, font=('times new roman', 10),
                                       bg='lightgray')
        self.edit_address_field.place(x=140, y=263)
        self.edit_address_field.delete("1.0", END)
        self.edit_address_field.insert(END, self.student_detail_row[8])

        apply_btn = Button(self.edit_detail_frame, text='Update', bg='#49a0ae', fg='white',
                           font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                           cursor='hand2', command=self.update_student_data)
        apply_btn.place(x=100, y=330, width=70, height=18)

        cancel_btn = Button(self.edit_detail_frame, text='Cancel', bg='#49a0ae', fg='white',
                            font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.edit_detail_cancel)
        cancel_btn.place(x=190, y=330, width=70, height=18)

        self.edit_date_field.bind('<ButtonRelease-1>', self.edit_date_selected)
        self.edit_month_field.bind('<ButtonRelease-1>', self.edit_month_selected)
        self.edit_year_field.bind('<ButtonRelease-1>', self.edit_year_selected)

    def edit_date_selected(self):
        self.edit_date_var.set("")

    def edit_month_selected(self):
        self.edit_month_var.set("")

    def edit_year_selected(self):
        self.edit_year_var.set("")

    # Pending - - Validate after user edit data & before saving into Database
    def update_student_data(self):
        if self.validate_edit_all_fields():

            if self.validate_edit_number_field():
                if self.is_valid_edit_email():

                    try:
                        self.connect_database()

                        self.cursor.execute(
                            "update student set enroll_no=%s, name=%s, email=%s, dob=%s, gender=%s, phone_no=%s, address=%s, depart_id=%s where enroll_no=%s",
                            (

                                self.edit_enroll_no_field.get(),
                                self.edit_name_field.get(),
                                self.edit_email_field.get(),
                                str(self.edit_year_field.get()) + "/" + str(self.edit_month_field.get()) + "/" + str(
                                    self.edit_date_field.get()),
                                self.edit_student_gender_combox.get(),
                                self.edit_phone_no_field.get(),
                                self.edit_address_field.get('1.0', END),
                                self.edit_enroll_no_field.get()[7] + self.edit_enroll_no_field.get()[8],
                                self.student_detail_row[1]
                            ))
                        self.con.commit()
                        self.update_page.destroy()
                        self.con.close()
                        messagebox.showinfo("Success", "Student Data updated Sucessfully")
                        self.fetch_student_data()
                    except Exception as ex:
                        self.update_page.destroy()
                        messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")
        else:
            print("validation of allFields Fails")

    def validate_edit_all_fields(self):
        if self.edit_name_field.get() == '':
            messagebox.showerror("Error", "Please enter full name to proceed", parent=self.update_page)

        elif self.edit_enroll_no_field.get() == '':
            messagebox.showerror("Error", "Please enter Enrollnment No. to proceed", parent=self.update_page)

        elif self.edit_email_field.get() == '':
            messagebox.showerror("Error", "Please enter Email to proceed", parent=self.update_page)

        elif self.edit_student_gender_combox.get() == '':
            messagebox.showerror("Error", "Please Select Your Gender to proceed", parent=self.update_page)

        elif (self.edit_date_field.get() == '' or self.edit_month_field.get() == ''
              or self.edit_year_field.get() == ''):
            messagebox.showerror("Error", "Please enter Date Of Birth to proceed", parent=self.update_page)

        elif self.edit_phone_no_field.get() == '':
            messagebox.showerror("Error", "Please enter Phone No. to proceed", parent=self.update_page)

        elif self.edit_address_field.get('1.0', END) == '':
            messagebox.showerror("Error", "Please enter Address to proceed", parent=self.update_page)

        else:
            return True

    def validate_edit_number_field(self):

        if ((self.edit_enroll_no_field.get().isdigit()) and (len(self.edit_enroll_no_field.get()) == 12)):
            if ((self.edit_phone_no_field.get().isdigit())) and (len(self.edit_phone_no_field.get()) == 10):
                if ((self.edit_date_field.get().isdigit()) and (self.edit_month_field.get().isdigit())
                        and (self.edit_year_field.get().isdigit()) and (len(self.edit_date_field.get()) == 2)
                        and (len(self.edit_month_field.get()) == 2) and (len(self.edit_year_field.get()) == 4)):
                    return True
                else:
                    messagebox.showerror("Error", "Please enter Date According To Format to proceed",
                                         parent=self.update_page)

            else:
                messagebox.showerror("Error", "Please enter 10 digit Phone No. to proceed",
                                     parent=self.update_page)

        else:
            messagebox.showerror("Error", "Please enter 12 digit Enrollnment No. to proceed", parent=self.update_page)

    def is_valid_edit_email(self):
        if len(self.edit_email_field.get()) > 10:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                        self.edit_email_field.get()) is not None:
                return True
            else:
                messagebox.showerror("Error", "Please enter valid Email id to proceed", parent=self.update_page)
                return False

    def edit_detail_cancel(self):
        self.edit_enroll_var.set("")
        self.edit_name_var.set("")
        self.edit_email_var.set("")
        self.edit_date_var.set("")
        self.edit_month_var.set("")
        self.edit_year_var.set("")
        self.edit_gender_var.set("")
        self.edit_phone_no_var.set("")
        self.update_page.destroy()

    def search_detail(self):
        try:
            # print(self.variable_b.get())
            self.connect_database()
            self.cursor.execute("select depart_id from department where department=%s", self.variable_b.get())
            id_row = self.cursor.fetchall()

            # print(cursor.execute("select depart_id from department where department=%s", self.variable_b.get()))
            self.cursor.execute("select * from student where depart_id=%s", id_row[0])

            rows = self.cursor.fetchall()
            print(rows)
            if rows == ():
                messagebox.showerror("Error", "No Student Found for Department ->" + self.variable_b.get())
            else:
                self.count_student_row.config(text=len(rows))
                self.show_department.config(text=self.variable_b.get())
                if len(rows) != 0:
                    self.student_data_table.delete(*self.student_data_table.get_children())
                    count = 1
                    for row in rows:
                        self.student_data_table.insert('', END, values=(
                        count, row[0], row[1], 0, row[5], row[2], row[4], row[3], row[6]))
                        count += 1
                    self.con.commit()
                self.con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")



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
        self.addTimeTableButton['state'] = 'normal'
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
        self.password_field = Entry(self.manage_user_frame, textvariable=self.user_pass_var,
                                    font=('times new roman', 12),
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

        # Count row
        count_row_label = Label(self.user_data_frame, text='No. Of User  :  ', font=('Goudy old style', 12, 'bold'),
                                fg='gray',
                                bg='white')
        count_row_label.place(x=30, y=20)
        self.count_row = Label(self.user_data_frame, text='', font=('Goudy old style', 12, 'bold'),
                               fg='gray',
                               bg='white')
        self.count_row.place(x=140, y=20)
        # search_Frame

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
        self.data_table = ttk.Treeview(table_frame, columns=("srno", "id", "name", "doj", "type"),
                                       xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=self.data_table.xview)
        scroll_vertical.config(command=self.data_table.yview)
        self.data_table.heading("srno", text="SrNo.")
        self.data_table.column("srno", width=50)
        self.data_table.heading("id", text="ID")
        self.data_table.column("id", width=90)
        self.data_table.heading("name", text="User Name")
        self.data_table.column("name", width=250)
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
            try:
                self.connect_database()
                if self.cursor.execute("select username from register where username=%s", self.id_field.get()):
                    messagebox.showerror("Error", "User Already Exist, Try Different Username")
                    self.clear()
                else:
                    self.cursor.execute("insert into register(username,date,usertype,password) values(%s,%s,%s,%s)",
                                        (
                                            self.id_field.get(),
                                            datetime.datetime.now().strftime('%Y-%m-%d'),
                                            self.user_type_combox.get(),
                                            self.password_field.get()
                                        ))

                    self.con.commit()
                    self.fetch_data()


                    self.store_registration_id()
                    self.clear()
                    messagebox.showinfo("sucess", "User Added Sucessfully.")
                ### base64.b64encode (pass)
                ### base64.b64decode (pass)
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")

    def store_registration_id(self):
        self.connect_database()
        self.cursor.execute("select reg_id from register where username=%s and usertype='Teacher'", self.id_field.get())
        registration_id = self.cursor.fetchall()
        # print(len(registration_id))
        if (len(registration_id) != 0):
            self.cursor.execute(
                "insert into teacher(reg_id, name, email, dob, gender, address, phone_no) values(%s, %s, %s, %s, %s, %s, %s)",
                (
                    str(registration_id[0][0]),
                    '',
                    '',
                    '',
                    '',
                    '',
                    ''
                ))
        self.con.commit()
        self.con.close()

    def fetch_data(self):
        try:
            self.connect_database()
            self.cursor.execute("select * from register")
            rows = self.cursor.fetchall()

            self.count_row.config(text=len(rows))
            self.data_table.delete(*self.data_table.get_children())
            count = 1
            for row in rows:
                self.data_table.insert('', END, values=(count, row[0], row[1], row[2], row[3]))
                self.con.commit()
                count += 1
            self.con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")

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
        self.user_id_var.set(self.row[2])
        self.user_type_combox.set(self.row[4])
        self.connect_database()
        self.cursor.execute("select password from register where reg_id=%s", self.row[1])
        password = self.cursor.fetchall()
        self.user_pass_var.set(password)
        self.con.commit()
        self.con.close()

    def update_data(self):
        print("Updating Selected Student.....")
        if self.id_field.get() == '' or self.user_type_combox.get() == '' or self.password_field.get() == '':
            messagebox.showerror("Error", "Select User From Table To Update", parent=self.manage_user_frame)
        else:
            try:
                self.connect_database()
                print("database connection done.....")
                self.cursor.execute(
                    "update register set username=%s, date=%s, usertype=%s, password=%s where reg_id=%s",
                    (
                        self.id_field.get(),
                        datetime.datetime.now().strftime('%Y-%m-%d'),
                        self.user_type_combox.get(),
                        self.password_field.get(),
                        self.row[1]
                    ))
                self.con.commit()
                self.con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("sucess", "User data Updated Sucessfully.")
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}\n Select User From Table To Update")
                self.clear()

    def delete_data(self):
        if self.id_field.get() == '' or self.user_type_combox.get() == '' or self.password_field.get() == '':
            messagebox.showerror("Error", "Select User From Table To Delete", parent=self.manage_user_frame)
        else:
            try:
                self.connect_database()
                self.cursor.execute("delete from register where reg_id=%s", self.row[1])
                self.con.commit()
                self.con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("sucess", "User Deleted Sucessfully.")
            except Exception as ex:
                messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}\n Select User From Table To Delete")
                self.clear()

    def search(self):
        self.connect_database()
        self.cursor.execute("select * from register where usertype=%s", self.searchby_usertype_var.get())
        rows = self.cursor.fetchall()
        self.count_row.config(text=len(rows))
        if len(rows) != 0:
            self.data_table.delete(*self.data_table.get_children())
            count = 1
            for row in rows:
                self.data_table.insert('', END, values=(count, row[0], row[1], row[2], row[3]))
                count += 1
            self.con.commit()
        self.con.close()

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
        self.addTimeTableButton['state'] = 'normal'
        self.trainButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'
        print('sucess')

    #### ============================================= Add Timetable      =============================================#####
    #### ==============================================================================================================#####
    def addTimeTableClicked(self):
        # os.system('train.py')
        self.changeable_frame.destroy()
        self.banner_title.destroy()

        self.banner_title = Label(self.banner_frame, text='Admin | TimeTable Page',
                                  font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.changeable_frame = Frame(self.admin_page, bg='#49a0ae')
        self.changeable_frame.place(x=160, y=55, height=680, width=1200)

        self.addTimeTableButton['state'] = 'disable'
        self.trainButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.checkDetailButton['state'] = 'normal'
        self.addUserButton['state'] = 'normal'
        self.addStudentButton['state'] = 'normal'

    #### ============================================= LOG OUT  =============================================######
    #### ==============================================================================================================#####
    def logoutClicked(self):
        self.user_logged_in_var.set("")
        with open('session_id.txt', 'w') as f:
            f.write("")

        self.admin_page.destroy()
        import main


root = Tk()
obj = Admin_Page(root)
root.mainloop()