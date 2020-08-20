from tkinter import *


class Main:
    def __init__(self,root):
        print(root)
        self.root=root
        self.root.title("AI-PHACS | Developed By : Sudip, Ayush, Bhavyesh, Preet, Jay | MiniDeveloper")
        # self.root.geometry('1200x900')
        self.root.state('zoomed')
        self.root.minsize()
        self.create_widgets()

    def create_widgets(self):

        #banner frame
        banner_frame = Frame(self.root, bg='#49a0ae', )
        banner_frame.place(relwidth=1, y=0, height=50)
        banner_title = Label(banner_frame, text='Home Page', font=('Impact', 20, 'bold'), bg='#49a0ae', fg='white')
        banner_title.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.normal_user = Button(root, text="USER",font=("times new roman", 15, 'bold'), bg='#49a0ae', fg='white',
                                  activebackground='#49a0ae', activeforeground='white', cursor='hand2',
                                  command=self.user_window)
        self.normal_user.place(relx=0.4, rely=0.5, anchor=CENTER,width=100,height=80)


        self.admin = Button(root, text="Admin", font=("times new roman", 15, 'bold'), bg='#49a0ae', fg='white',
                            activebackground='#49a0ae', activeforeground='white', cursor='hand2',
                            command=self.admin_window)
        self.admin.place(relx=0.6, rely=0.5, anchor=CENTER,width=100,height=80)

    def user_window(self):
        self.root.destroy()

        import user_login
        # print(user)


    def admin_window(self):
        self.root.destroy()
        import admin_login

root = Tk()
print(root)
obj = Main(root)
root.mainloop()