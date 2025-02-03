"""
Завдання 1
Напишіть програму, яка запитує у користувача ім'я та вік.
Після отримання даних програма повинна виводити привітання у форматі:
"Привіт, {ім'я}! Твій вік — {вік}".
Обробіть виняток, що виникає при введенні некоректного віку (вік < 0 або вік > 130),
і виведіть повідомлення про помилку.
"""

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
if user_age not in range(0, 130):
    raise Exception("Sorry, wrong age!")
else:
    print(f"Привіт, {user_name}! Твій вік - {user_age}")

"""Завдання 2
Реалізуйте перше завдання через функцію.
Функція повинна приймати ім'я і вік як параметри і повертати відформатований рядок.
Перевірка коректності отриманих даних повинна бути всередині функції.
Створіть дві версії реалізації функції:

Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції."""

# v1
def UserInfo(user_name, user_age):
    return f"Привіт, {user_name}! Твій вік - {user_age}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
if user_age not in range(0, 130):
    raise Exception("Sorry, wrong age!")
else:
    print(UserInfo(user_name, user_age))

# v2
def UserInfoWithTry(user_name, user_age):
    if user_age not in range(0, 130):
        raise Exception("Sorry, wrong age!")
    else:
        return f"Привіт, {user_name}! Твій вік - {user_age}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(UserInfoWithTry(user_name, user_age))

"""Завдання 3
Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних (число більше нуля) чисел.
Числа необхідно накопичувати у списку. Після отримання всіх значень програма повинна проаналізувати дані.
У разі виявлення від'ємного значення програма має згенерувати виняток. Якщо всі значення у списку позитивні,
програма має повернути на екран суму всіх чисел списку.
Згенерований виняток має бути оброблений кодом програми."""

list_of_numbers = []
while True:
    user_input = input(f"Enter a number for list or press \"Enter\" to exit: ")

    if user_input == "":
        print(f"List complete!\n"
              f"{'-' * 20}")
        break
    elif user_input != "":
        list_of_numbers.append(int(user_input))
        pass

if len(list_of_numbers) == 0:
    raise Exception("Sorry, no numbers in list!")

for number in list_of_numbers:
    if number < 0:
        raise Exception("Sorry, number is negative!")

print(f"Suma of list: {sum(list_of_numbers)}")

"""Завдання 4
Реалізуйте третє завдання через функцію.
Функція повинна приймати список як аргумент і повертати суму елементів списку.
Перевірка коректності отриманих даних повинна бути всередині функції.
Створіть дві версії реалізації функції:

Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції."""

# v1
def SumOfNumbersInList(list_of_numbers):
    return sum(list_of_numbers)

list_of_numbers.clear()
while True:
    user_input = input(f"Enter a number for list or press \"Enter\" to exit: ")

    if user_input == "":
        print(f"List complete!\n"
              f"{'-' * 20}")
        break
    elif user_input != "":
        list_of_numbers.append(int(user_input))
        pass

if len(list_of_numbers) == 0:
    raise Exception("Sorry, no numbers in list!")

for number in list_of_numbers:
    if number < 0:
        raise Exception("Sorry, number is negative!")

print(f"Suma of list: {SumOfNumbersInList(list_of_numbers)}")

# v2
def CheckListForNumbers(list_of_numbers):
    if len(list_of_numbers) == 0:
        raise Exception("Sorry, no numbers in list!")

    for number in list_of_numbers:
        if number < 0:
            raise Exception("Sorry, number is negative!")

    return sum(list_of_numbers)

list_of_numbers.clear()
while True:
    user_input = input(f"Enter a number for list or press \"Enter\" to exit: ")

    if user_input == "":
        print(f"List complete!\n"
              f"{'-' * 20}")
        break
    elif user_input != "":
        list_of_numbers.append(int(user_input))
        pass

print(f"Suma of list: {CheckListForNumbers(list_of_numbers)}")
