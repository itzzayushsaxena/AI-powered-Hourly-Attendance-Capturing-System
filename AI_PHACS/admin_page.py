from tkinter import *


class Admin_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-PHACS | Admin Page")
        self.root.state('zoomed')
        self.create_widgets()

    def create_widgets(self):
        self.studentPhoto = PhotoImage(file="images/newStudent.png")
        self.detailPhoto = PhotoImage(file="images/Detail.png")
        self.attendancePhoto = PhotoImage(file="images/attendance.png")
        # banner frame
        banner_frame = Frame(self.root, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Admin Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        btn_frame1 = Frame(self.root)
        btn_frame1.place(relwidth=1, y=90, height=240)
        btn_frame2 = Frame(self.root)
        btn_frame2.place(relwidth=1, y=380, height=240)


        addStudentButton = Button(btn_frame1, image=self.studentPhoto, command=self.addStudentClicked, border=0, height=190,
                              width=341)
        addStudentButton.place(relx=0.2, rely=0.5, anchor=CENTER)


        testButton = Button(btn_frame1, image=self.studentPhoto, command=self.addStudentClicked, border=0,
                                  height=190,
                                  width=341)
        testButton.place(relx=0.5, rely=0.5, anchor=CENTER)


        checkDetailButton = Button(btn_frame1, image=self.detailPhoto, command=self.addStudentClicked, border=0,
                                  height=190,
                                  width=341)
        checkDetailButton.place(relx=0.8, rely=0.5, anchor=CENTER)



        addUserButton = Button(btn_frame2, image=self.studentPhoto, command=self.addStudentClicked, border=0,
                                  height=190,
                                  width=341)
        addUserButton.place(relx=0.8, rely=0.5, anchor=CENTER)


        checkAttendanceButton = Button(btn_frame2, image=self.attendancePhoto, command=self.addStudentClicked, border=0,
                            height=190,
                            width=341)
        checkAttendanceButton.place(relx=0.5, rely=0.5, anchor=CENTER)


        checkDetailButton = Button(btn_frame2, image=self.studentPhoto, command=self.addStudentClicked, border=0,
                                   height=190,
                                   width=341)
        checkDetailButton.place(relx=0.2, rely=0.5, anchor=CENTER)

    def addStudentClicked(self):
        print("heloo")

root = Tk()
obj = Admin_Page(root)
root.mainloop()