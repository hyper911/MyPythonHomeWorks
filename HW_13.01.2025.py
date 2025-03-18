"""За допомогою Tkinter реалізуйте мінімальні можливості калькулятора"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calc")
root.geometry("230x300")
root.resizable(False, False)


def show_result():
    current_exp = entry.get()
    if current_exp.isalpha() == False:
        result = eval(current_exp)
        result = str(result)
        if result.find(".0") != -1:
            new_result = result.replace(".0", "")
            label["text"] = new_result
        else:
            label["text"] = result
        entry.delete(0, tk.END)
    else:
        Exception("Wrong input expression!")


def clear_entry():
    entry.delete(0, tk.END)
    label["text"] = "0"


def on_click(event):
    operations = "+-*/"
    button_text = event.widget.cget("text")
    if button_text == "C":
        clear_entry()
    elif button_text == "=":
        show_result()
    else:
        current_text = entry.get()
        if current_text != "":
            entry.delete(0, tk.END)
            entry.insert(0, current_text + str(button_text))
        elif current_text == "" and label["text"] != "0" and button_text in operations:
            entry.insert(0, str(label["text"]) + str(button_text))
        else:
            entry.delete(0, tk.END)
            entry.insert(0, str(button_text))


for r in range(5): root.rowconfigure(index=r, weight=0)
for c in range(5): root.columnconfigure(index=c, weight=0)

entry = ttk.Entry(root, width=30, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipadx=5, ipady=5)

label = ttk.Label(root, width=15, text="0", justify=tk.RIGHT, anchor=tk.E, font=("Arial", 13, "bold"))
label.grid(row=1, column=0, columnspan=5, padx=15, pady=5, ipadx=5, ipady=5, sticky="we")

stl_numbers = ttk.Style()
stl_numbers.configure("Num.TLabel", padding=[5], sticky="w", width="3", justify=tk.CENTER, anchor=tk.CENTER,
                      background="#bac5d6")
stl_numbers.map("Num.TLabel",
                foreground=[('pressed', 'red'), ('active', 'blue')],
                background=[('pressed', '!disabled', 'black'), ('active', 'white')],
                relief=[('pressed', 'sunken'),
                        ('!pressed', 'raised')])

stl_operations = ttk.Style()
stl_operations.configure("Op.TLabel", padding=[5], sticky="w", width="3", justify=tk.CENTER, anchor=tk.CENTER,
                         background="#f5eaba")
stl_operations.map("Op.TLabel",
                   foreground=[('pressed', 'red'), ('active', 'blue')],
                   background=[('pressed', '!disabled', 'blue'), ('active', 'white')],
                   relief=[('pressed', 'sunken'),
                           ('!pressed', 'raised')])

stl_eq = ttk.Style()
stl_eq.configure("Eq.TLabel", padding=[5], sticky="ns", width="3", justify=tk.CENTER, anchor=tk.CENTER,
                 background="#3db825")
stl_eq.map("Eq.TLabel",
           foreground=[('pressed', 'white'), ('active', 'red')],
           background=[('pressed', '!disabled', 'black'), ('active', 'white')],
           relief=[('pressed', 'sunken'),
                   ('!pressed', 'raised')])

stl_clear = ttk.Style()
stl_clear.configure("Cl.TLabel", padding=[5], sticky="we", width="3", justify=tk.CENTER, anchor=tk.CENTER,
                    background="#b84c25")
stl_clear.map("Cl.TLabel",
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'blue'), ('active', 'white')],
              relief=[('pressed', 'sunken'),
                      ('!pressed', 'raised')])

# Кнопки з числами
btn7 = ttk.Button(root, text="7", style="Num.TLabel")
btn7.grid(row=2, column=0, padx=2, pady=2, ipadx=5, ipady=5)
btn8 = ttk.Button(root, text="8", style="Num.TLabel")
btn8.grid(row=2, column=1, padx=2, pady=2, ipadx=5, ipady=5)
btn9 = ttk.Button(root, text="9", style="Num.TLabel")
btn9.grid(row=2, column=2, padx=2, pady=2, ipadx=5, ipady=5)
btn4 = ttk.Button(root, text="4", style="Num.TLabel")
btn4.grid(row=3, column=0, padx=2, pady=2, ipadx=5, ipady=5)
btn5 = ttk.Button(root, text="5", style="Num.TLabel")
btn5.grid(row=3, column=1, padx=2, pady=2, ipadx=5, ipady=5)
btn6 = ttk.Button(root, text="6", style="Num.TLabel")
btn6.grid(row=3, column=2, padx=2, pady=2, ipadx=5, ipady=5)
btn1 = ttk.Button(root, text="1", style="Num.TLabel")
btn1.grid(row=4, column=0, padx=2, pady=2, ipadx=5, ipady=5)
btn2 = ttk.Button(root, text="2", style="Num.TLabel")
btn2.grid(row=4, column=1, padx=2, pady=2, ipadx=5, ipady=5)
btn3 = ttk.Button(root, text="3", style="Num.TLabel")
btn3.grid(row=4, column=2, padx=2, pady=2, ipadx=5, ipady=5)
btn0 = ttk.Button(root, text="0", style="Num.TLabel")
btn0.grid(row=5, column=0, sticky="we", columnspan=2, padx=2, pady=2, ipadx=5, ipady=5)
btn_dot = ttk.Button(root, text=".", style="Num.TLabel")
btn_dot.grid(row=5, column=2, padx=2, pady=2, ipadx=5, ipady=5, sticky="w")

# Кнопки операцій
btn_div = ttk.Button(root, text="/", style="Op.TLabel")
btn_div.grid(row=2, column=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="w")
btn_mult = ttk.Button(root, text="*", style="Op.TLabel")
btn_mult.grid(row=3, column=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="w")
btn_sub = ttk.Button(root, text="-", style="Op.TLabel")
btn_sub.grid(row=4, column=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="w")
btn_add = ttk.Button(root, text="+", style="Op.TLabel")
btn_add.grid(row=5, column=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="w")

btn_eq = ttk.Button(root, text="=", style="Eq.TLabel", command=show_result)
btn_eq.grid(row=2, column=4, padx=2, pady=2, ipadx=5, ipady=5, sticky="ns", rowspan=5)
btn_clear = ttk.Button(root, text="C", style="Cl.TLabel")
btn_clear.grid(row=6, column=0, padx=2, pady=2, ipadx=5, ipady=5, sticky="we", columnspan=4)

root.bind_class("TButton", "<ButtonPress-1>", on_click)

root.mainloop()
