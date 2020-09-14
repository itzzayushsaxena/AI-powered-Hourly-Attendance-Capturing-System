from tkinter import *
import pymysql
from cryptography.fernet import Fernet


class User_Page:
    def __init__(self, root):
        self.user_page = root
        self.user_page.title("AI-PHACS | User Page")
        self.user_page.state('zoomed')
        self.create_widgets()

    def connect_database(self):
        self.con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
        self.cursor = self.con.cursor()

    def create_widgets(self):

        self.profilePhoto = PhotoImage(file="images/Start Training Final.png", master=self.user_page)
        self.checkAttendancePhoto = PhotoImage(file="images/Add Timetable Final.png", master=self.user_page)
        self.checkStudentDetailPhoto = PhotoImage(file="images/Add Student Final.png", master=self.user_page)
        self.logoutPhoto = PhotoImage(file="images/logout4.png", master=self.user_page)

        self.banner_frame = Frame(self.user_page, bg='#49a0ae', )
        self.banner_frame.place(x=155, relwidth=1, y=0, height=50)
        self.banner_title = Label(self.banner_frame, text='User | Profile', font=('Impact', 20, 'bold'), bg='#49a0ae',
                                  fg='white')
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

        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

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
        pass

    def checkAttendanceButtonClicked(self):
        pass

    def checkStudentDetailButtonClicked(self):
        pass

    def logoutClicked(self):
        self.user_logged_in_var.set("")
        with open('session_id.txt', 'w') as f:
            f.write("")
        self.user_page.destroy()
        import main


root = Tk()
obj = User_Page(root)
root.mainloop()
