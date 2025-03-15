"""Створіть примітивний дизайн вікна входу в додаток."""

from tkinter import *

HEIGHT = 550
WIDTH = 550

root = Tk()
root.title("Login form")
root.geometry("%dx%d" % (WIDTH, HEIGHT))
root.resizable(False, False)
root.option_add("*Font", "Roboto")
root.option_add("*Background", "#ebebeb")
img_back = PhotoImage(file="images/Div2_Logo.png")
bg_label = Label(root, image=img_back)
bg_label.place(relwidth=1, relheight=1)

frame = Frame(root, bd=10)
frame.place(relx=.5, rely=.2, relheight=.6, relwidth=.7, anchor='n')

# Sign in віджет
label = Label(frame, text="Вхід в додаток", font='16')
label.place(relwidth=1, relheight=.1)

# Login
label_login = Label(frame, text="Логін: ")
label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

login_register = Entry(frame)
login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

# Password
label_password = Label(frame, text="Пароль: ")
label_password.place(rely=0.4, relwidth=0.35, relheight=0.1)

password = Entry(frame, show='*')
password.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

# Button
button = Button(frame, text="Вхід")
button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

root.mainloop()
