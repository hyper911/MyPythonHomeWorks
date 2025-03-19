"""Зробіть валідацію пароля, для форми реєстрації.
Ваш пароль має мати:
1. І букви і цифри
2. СпецСимволи !?_
3.  На свій вибір
"""

from tkinter import *
from tkinter import messagebox
import pickle

HEIGHT = 550
WIDTH = 550


def registration():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=.5, rely=.2, relheight=.6, relwidth=.7, anchor='n')

    # sign in віджет
    label = Label(frame, text="Sign Up", font='16')
    label.place(relwidth=1, relheight=.1)

    # Login
    label_login = Label(frame, text="Login: ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    # Password
    label_password1 = Label(frame, text="Password: ")
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

    # Confirm pass
    label_password2 = Label(frame, text="Confirm Password: ")
    label_password2.place(rely=0.6, relwidth=0.35, relheight=0.1)

    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6, relwidth=0.55, relheight=0.1)

    # Button
    button = Button(frame, text="Sign Up", command=lambda: signup())
    button.place(relx=0.3, rely=0.85, relwidth=0.5, relheight=0.15)

    def signup():
        nonlocal label_error
        error = ""

        if label_error:
            # label.error.destroy()
            pass

        if len(login_register.get()) == 0:
            error = "*login error"
        elif len(password1.get()) < 6:
            error = "*password need minimum 6 character"
        elif not check_password(password1.get()):
            error = ("*password must contain at least 2 letters, 2 numbers and 1 special character")
        elif not password1.get() == password2.get():
            error = "*password error"
        else:
            save()

        label_error = Label(frame, text=error, fg="red", wraplength=350)
        label_error.place(rely=0.7)

    def save():
        data = dict()
        data[login_register.get()] = password1.get()
        f = open('login.txt', 'wb')
        pickle.dump(data, f)
        f.close()
        login_form()

    def check_password(password):
        spec_symbols = "!@#$%^&*()_-+={[}]|\\:;<>?.,/~` "
        count_alpha = count_digit = count_special = 0
        for i in password:
            if i.isalpha():
                count_alpha += 1
            if i.isdigit():
                count_digit += 1
            if i.isspace():
                count_special += 1
            if i in spec_symbols:
                count_special += 1
        if count_digit > 1 and count_special > 0 and count_alpha > 1:
            return True
        else:
            return False

def login_form():
    frame = Frame(root, bd=10)
    frame.place(relx=.5, rely=.2, relheight=.6, relwidth=.7, anchor='n')

    # Sign in віджет
    label = Label(frame, text="Sign In", font='16')
    label.place(relwidth=1, relheight=.1)

    # Login
    label_login = Label(frame, text="Login: ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    # Password
    label_password = Label(frame, text="Password: ")
    label_password.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password = Entry(frame, show='*')
    password.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

    # Button
    button = Button(frame, text="Sign In", command=lambda: login_pass())
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

    def login_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if login_register.get() in a and password.get() == a[login_register.get()]:
            messagebox.showinfo("Login Successful", "You are now logged in!")
        else:
            messagebox.showinfo("Login Failed", "You are not logged in!")

root = Tk()
root.title("Login form")
root.geometry("%dx%d" % (WIDTH, HEIGHT))
root.resizable(False, False)

root.option_add("*Font", "Calibri")
root.option_add("*Background", "white")

img = PhotoImage(file="images/Div2_Logo.png")
bg_label = Label(root, image=img)
bg_label.place(relwidth=1, relheight=1)

bt_singn_up = Button(root, bg="gold", text="SIGN UP", command=registration)
bt_singn_up.place(relx=0.2, rely=0.1, relwidth=0.3)

bt_singn = Button(root, bg="gold", text="SIGN UP", command=login_form)
bt_singn.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()
