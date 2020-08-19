from tkinter import *


class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("AI-PHACS | Developed By : Sudip, Ayush, Bhavyesh, Preet, Jay | MiniDeveloper")
        # self.root.geometry('1200x900')
        self.root.state('zoomed')
        self.root.minsize()
        self.create_widgets()

    def create_widgets(self):

        self.normal_user = Button(root, text="USER",font=("times new roman", 15, 'bold'), bg='gray', fg='white',
                                  activebackground='gray', activeforeground='white', cursor='hand2',
                                  command=self.user_window)
        self.normal_user.place(relx=0.4, rely=0.5, anchor=CENTER,width=100,height=80)


        self.admin = Button(root, text="Admin", font=("times new roman", 15, 'bold'), bg='gray', fg='white',
                            activebackground='gray', activeforeground='white', cursor='hand2',
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
obj = Main(root)
root.mainloop()