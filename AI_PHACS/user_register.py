from tkinter import *
from tkinter import ttk
import pymysql
import datetime


class User_Register:

    def __init__(self, root):
        self.add_user = root
        self.add_user.title("AI-PHACS | User Registration")
        self.add_user.state('zoomed')
        self.back = PhotoImage(file="images/back.png")
        self.create_widgets()

    def create_widgets(self):



        # banner frame
        banner_frame = Frame(self.add_user, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Manage User Page', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        #entry frame
        self.entry_frame = Frame(self.add_user, bg='white', )
        self.entry_frame.place(x=20 , y=80, width=550, height=450)

        backButton = Button(self.entry_frame, image=self.back, command=self.backClicked, border=0, height=60,
                            width=60, cursor='hand2', bg='white')
        backButton.place(x=20, y=20)

        sub_banner_frame = Frame(self.entry_frame, bg='#49a0ae', )
        sub_banner_frame.place(x=120, relwidth=1, y=26, height=50)
        sub_banner_title = Label(sub_banner_frame, text='Manage User', font=('Impact', 30, 'bold'), bg='#49a0ae',
                             fg='white')
        sub_banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        user_id = Label(self.entry_frame, text='Set UserName', font=('Goudy old style', 15, 'bold'), fg='gray',
                        bg='white')
        user_id.place(x=90, y=140)
        self.id_field = Entry(self.entry_frame, font=('times new roman', 15), bg='lightgray')
        self.id_field.place(x=90, y=170, width=350, height=35)

        password = Label(self.entry_frame, text='Set Password', font=('Goudy old style', 15, 'bold'), fg='gray',
                         bg='white')
        password.place(x=90, y=210)
        self.password_field = Entry(self.entry_frame,  font=('times new roman', 15), bg='lightgray')
        self.password_field.place(x=90, y=240, width=350, height=35)

        user_type = Label(self.entry_frame, text='User Type', font=('Goudy old style', 15, 'bold'), fg='gray', bg='white')
        user_type.place(x=90, y=280)
        self.user_type_chkbox = ttk.Combobox(self.entry_frame, font=('times new roman', 15), state='readonly')
        self.user_type_chkbox['values']=("Admin", "Teacher")
        self.user_type_chkbox.place(x=90, y=310, width=200, height=35)



        #button_frame

        self.btn_frame = Frame(self.entry_frame, bg='white', )
        self.btn_frame.place(relwidth=1, y=390, height=50)
        add_btn = Button(self.btn_frame, text='Add User', bg='#49a0ae', fg='white',
                           font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                           cursor='hand2', command=self.add_user_submit_clicked)
        add_btn.place(x=40, y=10, width=100, height=35)

        del_btn = Button(self.btn_frame, text='Delete User', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.manage_user_submit_clicked)
        del_btn.place(x=160, y=10, width=100, height=35)

        edit_btn = Button(self.btn_frame, text='Edit Data', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.manage_user_submit_clicked)
        edit_btn.place(x=280, y=10, width=100, height=35)

        clr_btn = Button(self.btn_frame, text='Clear Data', bg='#49a0ae', fg='white',
                         font=('times new roman', 14), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.manage_user_submit_clicked)
        clr_btn.place(x=400, y=10, width=100, height=35)


        #data frame

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
        self.user_type_combox = ttk.Combobox(self.data_frame, font=('times new roman', 15),  state='readonly')
        self.user_type_combox['values'] = ("Admin", "Teacher")
        self.user_type_combox.place(x=280, y=96, width=100, height=30,)

        search_btn = Button(self.data_frame, text='Search', bg='#49a0ae', fg='white',
                         font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                         cursor='hand2', command=self.manage_user_submit_clicked)
        search_btn.place(x=400, y=96, width=60, height=35)

        show_all_btn = Button(self.data_frame, text='Show All', bg='#49a0ae', fg='white',
                            font=('times new roman', 12), activebackground='#49a0ae', activeforeground='white',
                            cursor='hand2', command=self.manage_user_submit_clicked)
        show_all_btn.place(x=490, y=96, width=60, height=35)


        #Table Frame
        table_frame = Frame(self.data_frame, bd=4, relief=RIDGE, bg='white')
        table_frame.place(x=15, y=150, width=720, height=480)

        scroll_horizon = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_vertical = Scrollbar(table_frame, orient=VERTICAL)
        data_table = ttk.Treeview(table_frame,columns=("no", "id", "doj", "type"),xscrollcommand=scroll_horizon.set, yscrollcommand=scroll_vertical.set)
        scroll_horizon.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_horizon.config(command=data_table.xview)
        scroll_vertical.config(command=data_table.yview)
        data_table.heading("no", text="No.")
        data_table.column("no", width=90)
        data_table.heading("id", text="User Name")
        data_table.column("id", width=250)
        data_table.heading("doj", text="Date Of Joining")
        data_table.column("doj", width=150)
        data_table.heading("type", text="User Type")
        data_table['show'] = 'headings'
        data_table.pack(fill=BOTH, expand=1)

    def add_user_submit_clicked(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='ai_phacs')
        cursor = con.cursor()
        cursor.execute("insert into register values(%s,%s,%s,%s)",
                       (
                           self.id_field.get(),
                           self.password_field.get(),
                           datetime.datetime.now().strftime('%Y-%m-%d'),
                           self.user_type_chkbox.get()
                       ))
        con.commit()
        con.close()

    def manage_user_submit_clicked(self):
        print("ahfihais")



    def backClicked(self):
        print("register working")
        # self.add_user.destroy()
        # # self.root.deiconify()
        # # self.root.state('zoomed')


root = Tk()
obj = User_Register(root)
root.mainloop()