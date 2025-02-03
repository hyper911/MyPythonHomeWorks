"""Завдання 1
Напишіть програму, яка дозволяє користувачеві обчислити частку (ділення одного числа на інше) двох чисел.
Програма приймає два значення з клавіатури і повертає результат операції на екран.
Обробіть виняток, що виникає під час ділення на нуль, і виведіть повідомлення про помилку.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    print(a / b)
except ZeroDivisionError:
    print("Division by zero!")

"""Завдання 2
Реалізуйте перше завдання через функцію. Функція повинна приймати два параметри і відображати результат ділення на екран.
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.
"""

def dilWithoutExep(a, b):
    print(a / b)

def dilWithExcep(a, b):
    try:
        print(a / b)
    except:
        print("Division by zero in func!")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    dilWithoutExep(a, b)
except:
    print("Division by zero without func!")

dilWithExcep(a, b)

"""Завдання 3
Напишіть програму, яка приймає рядок і намагається перетворити його на число.
Обробіть виняток, що виникає при неможливості перетворення, і виведіть повідомлення про помилку.
"""

myStr = input("Enter a string: ")
try:
    print(int(myStr))
except ValueError:
    print("Value Error!")


"""Завдання 4
Реалізуйте третє завдання через функцію. Функція повинна приймати рядок і відображати результат перетворення на екран.
Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.
"""

def strToIntV1(myStr):
    print(int(myStr))

def strToIntV2(myStr):
    try:
        print(int(myStr))
    except ValueError:
        print("Value Error V2!")


myStr = input("Enter a string: ")
try:
    strToIntV1(myStr)
except ValueError:
    print("Value Error V1!")

strToIntV2(myStr)