from tkinter import *
from tkinter import messagebox
import sqlite3
from centerscreen import *


class DeleteBook(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.columnconfigure(3, weight=2)
        # ===== Entry =====
        self.l_search = Label(self, text="Search")
        self.l_search.grid(row=0, column=0, columnspan=3)

        self.e_search = Entry(self, width=70, justify="center")
        self.e_search.grid(row=1, column=0, columnspan=3, pady=5, padx=5)
        self.e_search.bind('<KeyRelease>', self.check)
        self.e_search.focus_set()

        # ===== Frame / Listbox =====
        self.f_listbox = Frame(self, relief='sunken')
        self.f_listbox.grid(row=2, column=0, padx=5, columnspan=3)

        self.listbox = Listbox(self.f_listbox, width=80)
        self.listbox.grid(row=0, column=0)
        self.listbox.bind("<<ListboxSelect>>", self.book_selection)
        # ===== Buttons =====
        self.b_delete = Button(self, text="Delete", width=30, command=self.delete_book)
        self.b_delete.grid(row=3, column=1, sticky='w', pady=5)
        self.b_destroy = Button(self, text='Exit', command=self.destroy, width=30)
        self.b_destroy.grid(row=3, column=2, sticky='w')

        # ===== Populate listbox =====
        self.listbox_data = []
        self.populate_listbox()
        self.data_to_delete = []

        self.update_list(self.listbox_data)
        # ===== ===== =====

    def book_selection(self, e):
        self.data_to_delete = self.listbox.get(ANCHOR).split(' - ')
        print(self.data_to_delete)

    def delete_book(self):
        conn = sqlite3.connect("library.db")
        sure_delete = messagebox.askquestion('Sure?', 'Are you sure?')
        if sure_delete == 'yes':
            conn.execute("DELETE FROM books WHERE title=?", (self.data_to_delete[0], ))
            data = self.listbox_data
            for index, item in enumerate(data):
                if self.data_to_delete[0] in item:
                    self.listbox_data.pop(index)
            self.update_list(self.listbox_data)
            conn.commit()
        else:
            pass
        conn.close()

    def check(self, e):
        typed = self.e_search.get()

        if typed == '':
            data = self.listbox_data
        else:
            data = []
            for item in self.listbox_data:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update_list(data)

    def populate_listbox(self):
        conn = sqlite3.connect("library.db")
        conn.execute("DROP VIEW IF EXISTS viewdata")
        conn.execute("CREATE VIEW IF NOT EXISTS viewdata "
                     "AS SELECT books.title AS title, authors.name AS aname, publisher.name AS pname "
                     "FROM books INNER JOIN authors ON books.author_id = authors._id "
                     "INNER JOIN publisher ON books.publisher_id = publisher._id")
        rows = conn.execute("SELECT title, aname, pname FROM viewdata")

        for title, author, publisher in rows:
            self.listbox_data.append(f'{title} - {author} - {publisher}')

        conn.close()

    def update_list(self, data=None):
        self.listbox.delete(0, END)

        for i in data:
            self.listbox.insert(END, i)


if __name__ == '__main__':
    app = DeleteBook()
    app.geometry(f'500x250+{x_p(app.winfo_screenwidth(), 400)}+{y_p(app.winfo_screenheight(), 400)}')
    app.mainloop()
