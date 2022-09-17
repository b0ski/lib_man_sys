import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from tkinter import *
from tkinter import messagebox
import pickle


from library.library import Library, Book


class LibraryResource:
    _library: Library = None

    def __init__(self, library: Library):
        self._library = library

    def add_book(self, req: BaseHTTPRequestHandler):
        self._library.add_book(Book("Harry Potter", "Fantasy", "J.K. Rowling"))

        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Andrey Varenyk', 'path': req.path,
                        'method': req.command, 'Library books': self._library.books.__str__()}).encode())

    def auth_reg(self, req: BaseHTTPRequestHandler):
        root = Tk()
        root.geometry("300x500")
        root.title("Login")

        def registration():
            text = Label(text="For entering library, please, sign up")
            text_log = Label(text="Enter login: ")
            reg_login = Entry()
            text_pass_1 = Label(text="Enter your password: ")
            reg_pass_1 = Entry()
            text_pass_2 = Label(text="Enter your password again: ")
            reg_pass_2 = Entry(show="*")
            button_reg = Button(text="Sign up", command=lambda: save())

            text.pack()
            text_log.pack()
            reg_login.pack()
            text_pass_1.pack()
            reg_pass_1.pack()
            text_pass_2.pack()
            reg_pass_2.pack()
            button_reg.pack()

            def save():
                login_pass_save = {}
                login_pass_save[reg_login.get()] = reg_pass_1.get()
                f = open("login.txt", "wb")
                pickle.dump(login_pass_save, f)
                f.close()
                login()

        def login():
            text_log = Label(text="Congrats")
            reg_login = Entry()
            text_enter_log = Label(text="Enter your login: ")
            enter_log = Entry()
            text_enter_pass = Label(text="Enter your password: ")
            enter_pass = Entry(show="*")
            button_enter = Button(text="Login", command=lambda: log_pass())

            text_log.pack()
            reg_login.pack()
            text_enter_log.pack()
            enter_log.pack()
            text_enter_pass.pack()
            enter_pass.pack()
            button_enter.pack()

            def log_pass():
                f = open('login.txt', "rb")
                a = pickle.load(f)
                f.close()
                if enter_log.get() in a:
                    if enter_pass.get() == a[enter_log.get()]:
                        messagebox.showinfo("Welcome!")
                    else:
                        messagebox.showerror("Error", "Login or password is incorrect")
                else:
                    messagebox.showerror("Error", "Login is incorrect")

        registration()

        root.mainloop()

        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Andrey Varenyk', 'path': req.path,
                        'method': req.command, 'Library books': self._library.books.__str__()}).encode())

