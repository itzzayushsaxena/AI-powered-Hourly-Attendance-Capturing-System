from tkinter import *


class Admin_Page:
    def __init__(self, root):
        self.admin_page = root
        self.admin_page.title("AI-PHACS | Admin Page")
        self.admin_page.state('zoomed')
        self.create_widgets()

    def create_widgets(self):
        self.studentPhoto = PhotoImage(file="images/newStudent.png")
        self.detailPhoto = PhotoImage(file="images/Detail.png")
        self.attendancePhoto = PhotoImage(file="images/attendance.png")
        self.back = PhotoImage(file="images/back.png")

        backButton = Button(self.admin_page, image=self.back, command=self.admin_page_backClicked, border=0, height=60,
                            width=60, cursor='hand2',)
        backButton.place(x=20, y=70)

        # banner frame
        banner_frame = Frame(self.admin_page, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Admin Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)



        btn_frame1 = Frame(self.admin_page)
        btn_frame1.place(relwidth=1, y=140, height=240)
        btn_frame2 = Frame(self.admin_page)
        btn_frame2.place(relwidth=1, y=410, height=240)


        addStudentButton = Button(btn_frame1, image=self.attendancePhoto, command=self.addStudentClicked, border=0, height=190,
                              width=341, cursor='hand2',)
        addStudentButton.place(relx=0.2, rely=0.5, anchor=CENTER)


        testButton = Button(btn_frame1, image=self.attendancePhoto, command=self.addStudentClicked, border=0,
                                  height=190, width=341, cursor='hand2',)
        testButton.place(relx=0.5, rely=0.5, anchor=CENTER)


        checkDetailButton = Button(btn_frame1, image=self.attendancePhoto, command=self.addStudentClicked, border=0,
                                  height=190, width=341, cursor='hand2',)
        checkDetailButton.place(relx=0.8, rely=0.5, anchor=CENTER)



        addUserButton = Button(btn_frame2, image=self.studentPhoto, command=self.addUserClicked, border=0,
                                  height=190, width=341, cursor='hand2',)
        addUserButton.place(relx=0.8, rely=0.5, anchor=CENTER)


        checkAttendanceButton = Button(btn_frame2, image=self.attendancePhoto, command=self.addStudentClicked, border=0,
                            height=190, width=341, cursor='hand2',)
        checkAttendanceButton.place(relx=0.5, rely=0.5, anchor=CENTER)


        checkDetailButton = Button(btn_frame2, image=self.attendancePhoto, command=self.addStudentClicked, border=0,
                                   height=190, width=341, cursor='hand2',)
        checkDetailButton.place(relx=0.2, rely=0.5, anchor=CENTER)

    def admin_page_backClicked(self):
        self.admin_page.destroy()
        import main

    def addStudentClicked(self):
        print("heloo")

#### USER REGISTRATION #####

    def addUserClicked(self):
        # self.admin_page.withdraw()
        # import user_register

root = Tk()
obj = Admin_Page(root)
root.mainloop()