from tkinter import *
from tkinter import messagebox
import sqlite3
from main import SystemStart
from centerscreen import *


class CheckUser(Tk):

    def __init__(self):
        # ===== Connect to database =====
        self.conn = sqlite3.connect('library.db')

        Tk.__init__(self)
        # ===== Label username =====
        self.l_username = Label(self, text='Username: ')
        self.l_username.grid(row=0, column=0)
        # ===== Label password =====
        self.l_password = Label(self, text='Password: ')
        self.l_password.grid(row=1, column=0)
        # ===== Entry username =====
        self.username = Entry(self)
        self.username.grid(row=0, column=1, sticky='we')

        # ===== Entry password =====
        self.password = Entry(self, show='*')
        self.password.grid(row=1, column=1, sticky='we')

        # ===== Button Login =====
        self.b_login = Button(self, text='Login', width=7, command=self.check_login)
        self.b_login.grid(row=2, column=1, sticky='w')

        # ===== Button Exit =====
        self.b_exit = Button(self, text='Exit', width=7, command=self.quit)
        self.b_exit.grid(row=2, column=1, sticky='e')
    #
    # def close_login(self):
    #     self.destroy()

    def check_login(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM login WHERE name=? AND pwrd=?", (self.username.get(), self.password.get()))
        user = cursor.fetchone()

        if self.username.get() and self.password.get():
            if user:

                mainWindow = SystemStart()
                mainWindow.title("Darling's Library")
                mainWindow.geometry(f"200x300+{80}+{200}")
                mainWindow.resizable(False, False)
                login.destroy()
                mainWindow.mainloop()
            else:
                messagebox.showinfo('Warning', 'Wrong username or password')
        else:
            messagebox.showinfo('Warning', 'Please, fill both fields')


login = CheckUser()
login.geometry(f"200x80+{x_p(login.winfo_screenwidth(), 400)}+{y_p(login.winfo_screenheight(), 300)}")
login.resizable(False, False)
login.mainloop()
