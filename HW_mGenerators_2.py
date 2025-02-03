from random import randint
import datetime

"""Завдання 1
Створіть функцію, яка повертає всі непарні числа в діапазоні.
Функція приймає початок і кінець діапазону як параметри.
Використовуйте механізм генераторів усередині функції."""

def OddNumbers(a, b):
    if b < a:
        x_min = b
        x_max = a
    else:
        x_min = a
        x_max = b
    l_e_numbers = list(filter(lambda x: x % 2 != 0, range(x_min, x_max)))
    return l_e_numbers

a = int(input(f"Start diapason: "))
b = int(input(f"End diapason: "))
print(OddNumbers(a, b))
print('-' * 15)

"""Завдання 2
Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем.
Функція приймає список, початок і кінець діапазону як параметри.
Використовуйте механізм генераторів усередині функції."""

def NotListNumbers(l, a, b):
    if b < a:
        x_min = b
        x_max = a
    else:
        x_min = a
        x_max = b
    l_gen = [randint(-500, 500) for x in range(50)]
    l_range = list(filter(lambda x: x not in range(x_min, x_max), l_gen))
    l = l_range
    del l_gen, l_range
    return l

l = []
a = int(input(f"Start diapason (from -500 to 500): "))
b = int(input(f"End diapason (from -500 to 500): "))
print(NotListNumbers(l, a, b))

"""Завдання 3
Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions).
Створіть функцію, що відображає лінію (горизонтальну або вертикальну) з використанням символу, зазначеного користувачем.
Користувач визначає символ і яку лінію відображати.

Сигнатура функції:
def show_line(symbol, function_to_call) 
symbol — символ для відображення.
function_to_call — функція для відтворення лінії
(вертикальна лінія або горизонтальна лінія, на один тип лінії — одна функція)."""

def PrintHorizontalLine(symbol):
    print(symbol * 10)

def PrintVerticalLine(symbol):
    for i in range(10):
        print(symbol)

def ShowLine(symbol, function_to_call):
    return function_to_call(symbol)

inp_symbol = input(f"Inut symbol: ")
inp_direction = input(f"Choose direction:\n"
                      f"1. Vertical\n"
                      f"2. Horizontal\n")
if inp_direction.startswith("1"):
    ShowLine(inp_symbol, PrintVerticalLine)
elif inp_direction.startswith("2"):
    ShowLine(inp_symbol, PrintHorizontalLine)
else:
    print("Invalid input")