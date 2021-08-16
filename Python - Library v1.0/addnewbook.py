import sqlite3
from tkinter import *
from tkinter import messagebox
from centerscreen import *


class ShowWindow(Tk):

    def __init__(self):
        # ===== Initiate Database =====
        self.conn = sqlite3.connect("library.db")

        # =======================
        Tk.__init__(self)
        # ===== Entry Title =====
        self.book_title_data = Entry(self, justify='center', width=45)
        self.book_title_data.grid(row=0, column=1, sticky='we', padx=10)
        # ===== Entry Author =====
        self.author_name_data = Entry(self, justify='center')
        self.author_name_data.grid(row=1, column=1, sticky='we', padx=10)
        # ===== Entry Price =====
        self.price_data = Entry(self, justify='center')
        self.price_data.grid(row=2, column=1, sticky='we', padx=10)
        # ===== Entry Publisher =====
        self.publisher_name_data = Entry(self, justify='center')
        self.publisher_name_data.grid(row=3, column=1, sticky='we', padx=10)

        # ===== Button Add =====
        self.b_add_database = Button(self, text='Add to Database', command=self.onclick)
        self.b_add_database.grid(row=4, column=1,  sticky='we', pady=5)

        self.b_close_window = Button(self, text="Close", command=self.close_window)
        self.b_close_window.grid(row=5, column=1, sticky='we')

        # ===== Labels =====
        self.label_book_title = Label(self, text="Book title:")
        self.label_book_title.grid(row=0, column=0, padx=10, pady=5)

        self.label_author = Label(self, text="Author:")
        self.label_author.grid(row=1, column=0, padx=10, pady=5)

        self.label_price = Label(self, text="Price:")
        self.label_price.grid(row=2, column=0, padx=10, pady=5)

        self.label_publisher = Label(self, text="Publisher:")
        self.label_publisher.grid(row=3, column=0, padx=10, pady=5)

    def close_window(self):
        self.destroy()

    def onclick(self):
        cursor_data = self.conn.cursor()
        cursor_data.execute("SELECT name FROM authors WHERE name=?", (self.author_name_data.get(),))
        row_authors = cursor_data.fetchone()
        cursor_data.execute("SELECT title FROM books WHERE title=?", (self.book_title_data.get(),))
        row_books = cursor_data.fetchone()
        cursor_data.execute("SELECT name FROM publisher WHERE name=?", (self.publisher_name_data.get(),))
        row_publisher = cursor_data.fetchone()

        if self.book_title_data.get() and self.author_name_data.get():
            if row_authors and row_books:
                messagebox.showinfo('Warning', 'Book already exist')
            else:
                if not row_authors:  # If author doesn't exist, add book and author to the database
                    if not row_publisher:  # If publisher doesn't exist, add to database
                        cursor_data.execute("INSERT INTO authors (name) VALUES (?)", (self.author_name_data.get(),))
                        cursor_data.execute("INSERT INTO publisher (name) VALUES (?)",
                                            (self.publisher_name_data.get(),))
                        cursor_data.execute("INSERT INTO books (title, price, author_id, publisher_id ) VALUES (?, ?, "
                                            "(SELECT _id FROM authors WHERE name = ?),"
                                            " (SELECT _id FROM publisher WHERE name = ?))",
                                            (self.book_title_data.get(), self.price_data.get(),
                                             self.author_name_data.get(), self.publisher_name_data.get()))
                    else:
                        cursor_data.execute("INSERT INTO authors (name) VALUES (?)", (self.author_name_data.get(),))
                        cursor_data.execute("INSERT INTO books (title, price, author_id, publisher_id ) VALUES (?, ?, "
                                            "(SELECT _id FROM authors WHERE name = ?),"
                                            " (SELECT _id FROM publisher WHERE name = ?))",
                                            (self.book_title_data.get(), self.price_data.get(),
                                             self.author_name_data.get(), self.publisher_name_data.get()))

                else:  # If author already exist, add book with author id to the data base
                    if not row_publisher:
                        cursor_data.execute("INSERT INTO publisher (name) VALUES (?)",
                                            (self.publisher_name_data.get(),))
                        cursor_data.execute("INSERT INTO books (title, price, author_id, publisher_id ) VALUES (?, ?, "
                                            "(SELECT _id FROM authors WHERE name = ?),"
                                            " (SELECT _id FROM publisher WHERE name = ?))",
                                            (self.book_title_data.get(), self.price_data.get(),
                                             self.author_name_data.get(), self.publisher_name_data.get()))
                    else:
                        cursor_data.execute("INSERT INTO books (title, price, author_id, publisher_id ) VALUES (?, ?, "
                                            "(SELECT _id FROM authors WHERE name = ?),"
                                            " (SELECT _id FROM publisher WHERE name = ?))",
                                            (self.book_title_data.get(), self.price_data.get(),
                                             self.author_name_data.get(), self.publisher_name_data.get()))
        else:
            messagebox.showinfo('', 'Please fill all boxes')
        print('Added to database')
        self.book_title_data.delete(0, END)
        self.author_name_data.delete(0, END)
        self.publisher_name_data.delete(0, END)
        self.price_data.delete(0, END)

        self.conn.commit()


if __name__ == "__main__":
    app = ShowWindow()
    app.title("Add new book")
    app.geometry(f"400x200+{x_p(app.winfo_screenwidth(), 400)}+{y_p(app.winfo_screenheight(), 300)}")
    app.resizable(False, False)
    app.columnconfigure(1, weight=2)
    app.columnconfigure(2, weight=2)
    app.columnconfigure(3, weight=1)
    app.mainloop()
