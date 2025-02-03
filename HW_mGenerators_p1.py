from random import randint
import datetime

"""Завдання 1
Створіть функцію, яка повертає всі парні числа в діапазоні.
Функція приймає початок і кінець діапазону як параметри.
Використовуйте механізм генераторів усередині функції."""

def EvenNumbers(a, b):
    if b < a:
        x_min = b
        x_max = a
    else:
        x_min = a
        x_max = b
    l_e_numbers = list(filter(lambda x: x % 2 == 0, range(x_min, x_max)))
    return l_e_numbers

a = int(input(f"Start diapason: "))
b = int(input(f"End diapason: "))
print(EvenNumbers(a, b))
print('-' * 15)

"""Завдання 2
Створіть функцію, яка повертає всі значення зі списку, що знаходяться в діапазоні, зазначеному користувачем.
Функція приймає список, початок і кінець діапазону як параметри.
Використовуйте механізм генераторів усередині функції."""

def ListNumbers(l, a, b):
    if b < a:
        x_min = b
        x_max = a
    else:
        x_min = a
        x_max = b
    l_gen = list(map(lambda x: x, range(x_min, x_max + 1)))
    l = l_gen
    del l_gen
    return l

l = []
a = int(input(f"Start diapason: "))
b = int(input(f"End diapason: "))
print(ListNumbers(l, a, b))

"""Завдання 3
Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions).
Створіть функцію, яка перевіряє на парність або непарність передане число.
Користувач визначає на що перевіряти (парність або непарність).

Сигнатура функції:
def check_value(value_to_check, function_to_call)

value_to_check — значення для перевірки.
function_to_call — функція перевірки (функція для перевірки на парність або функція для перевірки на непарність)."""

def OddOrEven(a):
    even_odd = input(f"Choose from menu: \n"
                     f"1. Even \n"
                     f"2. Odd \n")
    if even_odd.startswith("1"):
        return a % 2 == 0
    elif even_odd.startswith("2"):
        return a % 2 != 0
    else:
        return False

def Check_Value(a, check_func):
    return check_func(a)

a = int(input(f"Enter the integer: "))
print(f"Integer is even: {Check_Value(a, OddOrEven)}")

"""Завдання 4
Створіть функцію для відображення поточного часу. Функція не приймає параметрів.
Не використовуючи синтаксис декораторів, виконайте декорування функції за допомогою іншої функції.
Потенційне виведення даних на екран:

***************************
23:00
***************************

У цьому виведенні на екран дві лінії із зірочок — результати декорування.
"""

def ViewTime():
    print(datetime.datetime.now().strftime("%H:%M"))

def PrintTimeWithDecor():
    print('*' * 27)
    ViewTime()
    print('*' * 27)

PrintTimeWithDecor()
