from tkinter import *
import re
from tkinter import ttk
from tkinter import messagebox
from sessionGenerator import readId
from database import connect_database
from dataTypeConversion import tupleToList

class User_Page:
    def __init__(self, root):
        self.user_page = root
        self.user_page.title("AI-PHACS | User Page")
        self.user_page.state('zoomed')
        self.create_widgets()

    def connect_database(self):
        result = connect_database()
        self.con = result[0]
        self.cursor = result[1]

    def create_widgets(self):
        self.profilePhoto = PhotoImage(file="images/Profile 3.png", master=self.user_page)
        self.checkAttendancePhoto = PhotoImage(file="images/Check Attendance Final.png", master=self.user_page)
        self.checkStudentDetailPhoto = PhotoImage(file="images/Check Details Final.png", master=self.user_page)
        self.logoutPhoto = PhotoImage(file="images/logout4.png", master=self.user_page)

        # banner frame
        self.banner_frame = Frame(self.user_page, bg='#49a0ae', )
        self.banner_frame.place(x=155, relwidth=1, y=0, height=50)
        self.banner_title = Label(self.banner_frame, text='User | Profile', font=('Impact', 20, 'bold'), bg='#49a0ae',
                                  fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

        row_name = readId()
        self.user_logged_in_var = StringVar()
        if (len(row_name) != 0):
            self.user_logged_in_var.set(row_name[0][0])

        logout_label = Label(self.banner_frame, text="Welcome,  ", font=('times new roman', 10, 'bold'),
                             bg='#49a0ae',
                             fg='white')
        logout_label.place(x=970, y=1)
        logout_label = Label(self.banner_frame, textvariable=self.user_logged_in_var,
                             font=('times new roman', 15, 'bold'), bg='#49a0ae',
                             fg='white')
        logout_label.place(x=990, y=19)

        logoutButton = Button(self.banner_frame, image=self.logoutPhoto, command=self.logoutClicked, border=0,
                              height=45,
                              width=45, cursor='hand2', bg='#49a0ae', activebackground='#49a0ae', )
        logoutButton.place(x=1150, y=5)

        ###### FRAMES

        self.btn_frame = Frame(self.user_page, bg=None)
        self.btn_frame.place(x=5, relheight=1, width=150)

        self.changeable_frame = Frame(self.user_page, bg='white')
        self.changeable_frame.place(x=165, y=60, height=675, width=1190)
        self.user_template()

    def user_template(self):
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

        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        self.profileButton = Button(interior, image=self.profilePhoto,
                                            command=self.draw_user_profile_page,
                                            border=0,
                                            height=120, width=120, cursor='hand2', state='disable')
        self.profileButton.pack(padx=0, pady=5, side=TOP)

        self.checkAttendanceButton = Button(interior, image=self.checkAttendancePhoto, command=self.checkAttendanceButtonClicked, border=0,
                                    height=120, width=120, cursor='hand2', )
        self.checkAttendanceButton.pack(padx=0, pady=5, side=TOP)

        self.checkStudentDetailButton = Button(interior, image=self.checkStudentDetailPhoto, command=self.checkStudentDetailButtonClicked, border=0,
                                       height=120,
                                       width=120, cursor='hand2', )
        self.checkStudentDetailButton.pack(padx=0, pady=5, side=TOP)


        self.checkAttendanceButton['state'] = 'normal'
        self.checkStudentDetailButton['state'] = 'normal'
        self.draw_user_profile_page()

    def draw_user_profile_page(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()
        self.banner_title = Label(self.banner_frame, text='User | Profile', font=('times new roman', 20, 'bold'), bg='#49a0ae',
                                  fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.changeable_frame = Frame(self.user_page, bg='white')
        self.changeable_frame.place(x=165, y=60, height=675, width=1190)

        self.btn_frame = Frame(self.changeable_frame, bg='white')
        self.btn_frame.place(x=90, y=40, height=80, width=245)

        self.profile_frame = Frame(self.changeable_frame, bg='white', bd=4, relief=RIDGE)
        self.profile_frame.place(x=90, y=105, height=550, width=1000)

        ## Variable

        self.edit_name_var = StringVar()
        self.edit_email_var = StringVar()
        self.edit_dob_var = StringVar()
        self.edit_date_var = StringVar()
        self.edit_month_var = StringVar()
        self.edit_year_var = StringVar()
        self.edit_gender_var = StringVar()
        self.edit_address_var = StringVar()
        self.edit_phone_no_var = StringVar()
        self.subject_name_var = StringVar()
        self.subject_name = StringVar()

        profile_edit_btn = Button(self.btn_frame, text='Edit Profile', bg='#49a0ae', fg='white',
                                     font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                                     cursor='hand2', command=self.edit_profile)
        profile_edit_btn.place(x=5, y=15, width=100, height=22)
        edit_password = Button(self.btn_frame, text='Edit Password', bg='#49a0ae', fg='white',
                               font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                               cursor='hand2', )
        edit_password.place(x=120, y=15, width=110, height=22)

        self.fetch_teacher_data()



        Label(self.profile_frame, text='User Name :', font=('times new roman', 12), bg='white',
                       fg='black').place(x=20, y=15)
        username = Label(self.profile_frame, textvariable=self.user_logged_in_var, font=('times new roman', 12), bg='white',
                         fg='black')
        username.place(x=120, y=15)
        Label(self.profile_frame, text='Full Name:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=40)
        fullname = Label(self.profile_frame, textvariable=self.edit_name_var, font=('times new roman', 12), bg='white',
                         fg='black')
        fullname.place(x=120, y=40)
        Label(self.profile_frame, text='Subjects ', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=80)
        subjects = Label(self.profile_frame, textvariable=self.subject_name, font=('times new roman', 12), bg='white',
                         fg='black')
        subjects.place(x=120, y=80)
        Label(self.profile_frame, text='Address:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=120)
        address = Label(self.profile_frame, textvariable=self.edit_address_var, font=('times new roman', 12), bg='white',
                         fg='black')
        address.place(x=120, y=120)
        Label(self.profile_frame, text='Phone No:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=160)
        phone_no = Label(self.profile_frame, textvariable=self.edit_phone_no_var, font=('times new roman', 12), bg='white',
                         fg='black')
        phone_no.place(x=120, y=160)
        Label(self.profile_frame, text='Email:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=240)
        email = Label(self.profile_frame, textvariable=self.edit_email_var, font=('times new roman', 12), bg='white',
                         fg='black')
        email.place(x=120, y=240)
        Label(self.profile_frame, text='Gender:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=300)
        gender = Label(self.profile_frame, textvariable=self.edit_gender_var, font=('times new roman', 12), bg='white',
                         fg='black')
        gender.place(x=120, y=300)
        Label(self.profile_frame, text='DOB:', font=('times new roman', 12), bg='white',
                         fg='black').place(x=20, y=340)
        dob = Label(self.profile_frame, textvariable=self.edit_dob_var, font=('times new roman', 12), bg='white',
                         fg='black')
        dob.place(x=120, y=340)


        self.profileButton['state'] = 'disable'
        self.checkAttendanceButton['state'] = 'normal'
        self.checkStudentDetailButton['state'] = 'normal'

    def edit_profile_frame_close(self):
        self.edit_profile_frame.destroy()
        self.fetch_teacher_data()

    def fetch_teacher_data(self):
        self.connect_database()
        self.cursor.execute("select reg_id from register where username=%s", self.user_logged_in_var.get())
        self.register_id = self.cursor.fetchall()
        self.cursor.execute("select * from teacher where reg_id=%s", self.register_id[0][0])
        teacher_info = self.cursor.fetchall()
        self.cursor.execute("select teacher_id from teacher where reg_id=%s", self.register_id[0][0])
        self.teacher_id = self.cursor.fetchall()
        self.teacher_id = self.teacher_id[0][0]
        self.cursor.execute("select subject_id from assigned_subjects where teacher_id=%s", self.teacher_id)
        subjectid_tuple = self.cursor.fetchall()
        subjectid_list = tupleToList(subjectid_tuple)

        subject_name = []
        subject_list = []
        for subject in subjectid_list:
            self.cursor.execute("select subject from subject where subject_id=%s", subject)
            subject_name += self.cursor.fetchall()
        for count in range(0, len(subject_name)):
            subject_list.append(subject_name[count][0])
        self.con.commit()
        self.con.close()


        self.edit_name_var.set(teacher_info[0][2])
        self.edit_email_var.set(teacher_info[0][3])
        self.edit_dob_var.set(teacher_info[0][4])
        edit_dob = teacher_info[0][4]
        self.edit_date_var.set(format(edit_dob.day, '02'))
        self.edit_month_var.set(format(edit_dob.month, '02'))
        self.edit_year_var.set(edit_dob.year)
        self.edit_gender_var.set(teacher_info[0][5])
        self.edit_address_var.set(teacher_info[0][6])
        self.edit_phone_no_var.set(teacher_info[0][7])
        self.subject_name.set('')
        for subject in subject_list:
            self.subject_name.set(self.subject_name.get() + str(subject) + ' , ')

    def edit_profile(self):
        self.edit_profile_frame = Toplevel(self.profile_frame)
        self.edit_profile_frame.title("AI-PHACS | Edit Profile")
        self.edit_profile_frame.geometry('385x420+540+250')
        self.edit_detail_frame = Frame(self.edit_profile_frame, bg=None, )
        self.edit_detail_frame.place(x=5, y=25, width=375, height=375)

        Label(self.edit_detail_frame, text='Complete Your Profile', font=('Goudy old style', 15, 'bold'),
                               fg='black', bg=None).place(x=90, y=0)

        fullname = Label(self.edit_detail_frame, text='FullName ', font=('Goudy old style', 10, 'bold'),
                                  fg='gray',
                                  bg=None)
        fullname.place(x=50, y=50)
        self.fullname_field = Entry(self.edit_detail_frame, textvariable=self.edit_name_var,
                                     font=('times new roman', 10), bg='lightgray')
        self.fullname_field.place(x=140, y=53, width=170, height=18)
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

        self.edit_date_field = Entry(self.edit_detail_frame,textvariable=self.edit_date_var,
                                     font=('times new roman', 10),
                                     bg='lightgray')

        self.edit_date_field.place(x=140, y=140, width=30, height=18)

        slash1 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash1.place(x=185, y=137)
        self.edit_month_field = Entry(self.edit_detail_frame,textvariable=self.edit_month_var,
                                      font=('times new roman', 10),
                                      bg='lightgray')
        self.edit_month_field.place(x=205, y=140, width=30, height=18)
        slash2 = Label(self.edit_detail_frame, text='/', font=('Goudy old style', 11), bg=None, fg='gray')
        slash2.place(x=250, y=137)
        self.edit_year_field = Entry(self.edit_detail_frame,textvariable=self.edit_year_var,
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
        self.edit_address_field.insert(END, self.edit_address_var.get())

        next_btn = Button(self.edit_detail_frame, text='Lock & Next', bg='#49a0ae', fg='white',
                           font=('times new roman', 10), activebackground='#49a0ae', activeforeground='white',
                           cursor='hand2', command=self.next_page)
        next_btn.place(x=150, y=350, width=90, height=18)

        self.edit_profile_frame.protocol("WM_DELETE_WINDOW", self.edit_profile_frame_close)

    def next_page(self):

        if self.validate_edit_all_fields():
            if self.validate_edit_number_field():
                if self.is_valid_edit_email():
                    try:
                        self.connect_database()
                        self.cursor.execute(
                            "update teacher set name=%s, email=%s, dob=%s, gender=%s, phone_no=%s, address=%s where reg_id=%s",
                            (

                                self.fullname_field.get(),
                                self.edit_email_field.get(),
                                str(self.edit_year_field.get()) + "/" + str(self.edit_month_field.get()) + "/" + str(
                                    self.edit_date_field.get()),
                                self.edit_student_gender_combox.get(),
                                self.edit_phone_no_field.get(),
                                self.edit_address_field.get('1.0', END),
                                self.register_id[0][0]
                            ))
                        self.con.commit()
                        self.edit_detail_frame.destroy()
                        self.con.close()
                        self.fetch_teacher_data()
                    except Exception as ex:
                        messagebox.showerror("Error", f"Action Failed Due To : {str(ex)}")
                        self.edit_profile_frame.destroy()

                    self.edit_detail_frame = Frame(self.edit_profile_frame, bg=None, )
                    self.edit_detail_frame.place(x=5, y=5, width=375, height=410)
                    self.subject_name_var = StringVar()
                    self.total = StringVar()
                    self.subject_name_var.set('')
                    # database connetion pending
                    self.connect_database()
                    self.cursor.execute("select count(*) from subject")
                    self.total.set(self.cursor.fetchall()[0][0])
                    self.con.close()
                    Label(self.edit_detail_frame, text='(Please Select Your Subjects. you can scroll through list)',
                          font=('Goudy old style', 12, 'bold'),
                          fg='black', bg=None).place(x=5, y=0)
                    Label(self.edit_detail_frame, text='Subjects Selected: ', font=('Goudy old style', 12, 'bold'),
                          fg='gray', bg=None).place(x=20, y=30)
                    Label(self.edit_detail_frame, text='Total Subjects: ', font=('Goudy old style', 12, 'bold'),
                          fg='gray', bg=None).place(x=20, y=50)
                    subject_selected = Label(self.edit_detail_frame, textvariable=self.subject_name_var,
                                             font=('Goudy old style', 12, 'bold'),
                                             fg='gray',
                                             bg=None)
                    subject_selected.place(x=150, y=30)
                    total_subjects = Label(self.edit_detail_frame, textvariable=self.total,
                                           font=('Goudy old style', 12, 'bold'),
                                           fg='gray',
                                           bg=None)
                    total_subjects.place(x=120, y=50)

                    # LIST Box
                    self.lb = Listbox(self.edit_detail_frame, selectmode=MULTIPLE, bd=4, relief=RIDGE, )

                    self.lb.place(x=20, y=70, width=300, height=250)
                    self.connect_database()
                    self.cursor.execute("select subject from subject")
                    subjects = self.cursor.fetchall()
                    data = []
                    for subject in subjects:
                        data.append(subject[0])

                    for item in data:
                        self.lb.insert(END, item)
                    apply_btn = Button(self.edit_detail_frame, text='lock Choices', bg='#49a0ae', fg='white',
                                       font=('times new roman', 10), activebackground='#49a0ae',
                                       activeforeground='white',
                                       cursor='hand2', command=self.apply)
                    apply_btn.place(x=20, y=330, width=75, height=18)
                    submit = Button(self.edit_detail_frame, text='Submit The Form', bg='#49a0ae', fg='white',
                                    font=('times new roman', 13), activebackground='#49a0ae', activeforeground='white',
                                    cursor='hand2', command=self.submit_form)
                    submit.place(x=120, y=360, width=130, height=25)

                else:
                    print("is_valid_edit_email fails")
            else:
                print("validate_edit_number_field fails")
        else:
            print("validation of allFields Fails")



    def validate_edit_all_fields(self):
        if self.fullname_field.get() == '':
            messagebox.showerror("Error", "Please enter full name to proceed", parent=self.edit_profile_frame)

        elif self.edit_email_field.get() == '':
            messagebox.showerror("Error", "Please enter Email to proceed", parent=self.edit_profile_frame)

        elif self.edit_student_gender_combox.get() == '':
            messagebox.showerror("Error", "Please Select Your Gender to proceed", parent=self.edit_profile_frame)

        elif (self.edit_date_field.get() == '' or self.edit_month_field.get() == ''
              or self.edit_year_field.get() == ''):
            messagebox.showerror("Error", "Please enter Date Of Birth to proceed", parent=self.edit_profile_frame)

        elif self.edit_phone_no_field.get() == '':
            messagebox.showerror("Error", "Please enter Phone No. to proceed", parent=self.edit_profile_frame)

        elif self.edit_address_field.get('1.0', END) == '':
            messagebox.showerror("Error", "Please enter Address to proceed", parent=self.edit_profile_frame)

        else:
            return True

    def validate_edit_number_field(self):

        if ((self.edit_phone_no_field.get().isdigit())) and (len(self.edit_phone_no_field.get()) == 10):
            if ((self.edit_date_field.get().isdigit()) and (self.edit_month_field.get().isdigit())
                    and (self.edit_year_field.get().isdigit()) and (len(self.edit_date_field.get()) == 2)
                    and (len(self.edit_month_field.get()) == 2) and (len(self.edit_year_field.get()) == 4)):
                return True
            else:
                messagebox.showerror("Error", "Please enter Date According To Format to proceed",
                                     parent=self.edit_profile_frame)

        else:
            messagebox.showerror("Error", "Please enter 10 digit Phone No. to proceed",
                                 parent=self.edit_profile_frame)


    def is_valid_edit_email(self):
        if len(self.edit_email_field.get()) > 10:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                        self.edit_email_field.get()) is not None:
                return True
            else:
                messagebox.showerror("Error", "Please enter valid Email id to proceed", parent=self.edit_profile_frame)
                return False

    def apply(self):
        self.subject_name_var.set(len(self.lb.curselection()))

    def submit_form(self):
        subject_name_list = []
        for item in self.lb.curselection():
            subject_name_list.append(str(self.lb.get(item)))

        subject_id = ()
        subjectid_list = []
        self.connect_database()
        count = 0
        for subject in subject_name_list:
            self.cursor.execute("select subject_id from subject where subject=%s", subject)
            subject_id += self.cursor.fetchall()
            subjectid_list.append(subject_id[count][0])
            count += 1
        self.con.commit()
        self.con.close()
        if not subjectid_list:
            messagebox.showerror("Error", "Please Select Your Subjects.", parent=self.edit_detail_frame)
        else:
            self.connect_database()
            self.cursor.execute("delete from assigned_subjects where teacher_id=%s", self.teacher_id)
            self.con.commit()
            self.con.close()
            self.connect_database()
            for id in subjectid_list:
                self.cursor.execute("insert into assigned_subjects(teacher_id,subject_id)"
                                    "values(%s,%s)",
                                    (
                                        self.teacher_id,
                                        id
                                    ))
                self.con.commit()
            self.con.close()
            self.edit_profile_frame.destroy()
            self.fetch_teacher_data()
            messagebox.showinfo("Sucess", "Profile Updated Sucessfully.", parent=self.profile_frame)

    def checkAttendanceButtonClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()
        self.banner_title = Label(self.banner_frame, text='User | Student Attendance Page', font=('times new roman', 20, 'bold'),
                                  bg='#49a0ae',
                                  fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.changeable_frame = Frame(self.user_page, bg='white')
        self.changeable_frame.place(x=165, y=60, height=675, width=1190)

        self.profileButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'disable'
        self.checkStudentDetailButton['state'] = 'normal'

    def checkStudentDetailButtonClicked(self):
        self.changeable_frame.destroy()
        self.banner_title.destroy()
        self.banner_title = Label(self.banner_frame, text='User | Student Detail Page', font=('times new roman', 20, 'bold'),
                                  bg='#49a0ae',
                                  fg='white')
        self.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.changeable_frame = Frame(self.user_page, bg='white')
        self.changeable_frame.place(x=165, y=60, height=675, width=1190)

        self.profileButton['state'] = 'normal'
        self.checkAttendanceButton['state'] = 'normal'
        self.checkStudentDetailButton['state'] = 'disable'

    def logoutClicked(self):
        self.user_logged_in_var.set("")
        with open('session_id.txt', 'w') as f:
            f.write("")
        self.user_page.destroy()
        import main



root = Tk()
obj = User_Page(root)
root.mainloop()
