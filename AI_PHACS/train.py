
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.
# File is Made For Testing Purpose Only.

import admin_page
from tkinter import *

admin_page.changeable_frame.destroy()
admin_page.banner_title.destroy()

admin_page.banner_title = Label(admin_page.banner_frame, text='Admin | Training Page',
                          font=('times new roman', 20, 'bold'), bg='#49a0ae', fg='white')
admin_page.banner_title.place(relx=0.4, rely=0.5, anchor=CENTER)

admin_page.changeable_frame = Frame(admin_page, bg='#49a0ae')
admin_page.changeable_frame.place(x=160, y=55, height=680, width=1200)

admin_page.trainButton['state'] = 'disable'
admin_page.checkAttendanceButton['state'] = 'normal'
admin_page.checkDetailButton['state'] = 'normal'
admin_page.addUserButton['state'] = 'normal'
admin_page.addStudentButton['state'] = 'normal'