from tkinter import *
from addnewbook import *
from search import *
from delete import *
# Functions


def call_add_book():
    app = ShowWindow()
    app.title("Add new book")
    app.geometry(f"400x200+{x_p(app.winfo_screenwidth(), 400)}+{y_p(app.winfo_screenheight(), 300)}")
    app.resizable(False, False)
    app.columnconfigure(1, weight=2)
    app.columnconfigure(2, weight=2)
    app.columnconfigure(3, weight=1)
    app.mainloop()


def call_search_book():
    search_book = SearchBook()
    search_book.geometry(f'600x420+'
                         f'{x_p(search_book.winfo_screenwidth(), 600)}+{y_p(search_book.winfo_screenheight(), 420)}')
    search_book.title('Search book')
    search_book.resizable(False, False)
    search_book.mainloop()


def call_delete_book():
    delete_book = DeleteBook()
    delete_book.title("Delete book")
    delete_book.geometry(f'500x250+'
                         f'{x_p(delete_book.winfo_screenwidth(), 500)}+{y_p(delete_book.winfo_screenheight(), 250)}')
    delete_book.mainloop()


class SystemStart(Tk):

    def __init__(self):
        Tk.__init__(self)
        # ===== Label text =====
        self.info_label = Label(self, text="What do you need?", font=('Verdana', 12), relief='sunken')
        self.info_label.grid(row=0, padx=10, pady=10)

        # ===== Button Add =====
        self.b_add = Button(self, text='Add', command=call_add_book)
        self.b_add.grid(row=1, sticky='we', padx=20, pady=5)
        # ===== Button Search =====
        self.b_search = Button(self, text='Search', command=call_search_book)
        self.b_search.grid(row=2, sticky='we', padx=20, pady=5)
        # ===== Button Log out =====
        self.b_delete = Button(self, text='Delete', command=call_delete_book)
        self.b_delete.grid(row=3, sticky='we', padx=20, pady=5)
        # ===== Button Exit =====
        self.b_quit = Button(self, text='Exit', command=quit)
        self.b_quit.grid(row=4, sticky='we', padx=20, pady=5)


if __name__ == "__main__":
    mainWindow = SystemStart()
    mainWindow.title("Darling's Library")
    mainWindow.geometry(f"200x300+{80}+{200}")
    mainWindow.resizable(False, False)
    mainWindow.mainloop()
