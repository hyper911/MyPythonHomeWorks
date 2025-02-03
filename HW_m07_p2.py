"""Завдання 1
Напишіть програму, яка запитує у користувача число і обчислює його факторіал.
Обробіть виняток, що виникає при введенні від'ємного числа, і виведіть повідомлення про помилку."""

a = int(input(f"Enter a number: "))
if a < 0:
    raise Exception("Number cannot be negative!")
fact = 1
for i in range(1, a + 1):
    fact = fact * i

print(f"Factorial of {a} is {fact}")

"""Завдання 2
Реалізуйте перше завдання через функцію. Функція повинна приймати число як параметр і повертати його факторіал.
Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції."""

# v1
def factorialCalculation(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

a = int(input(f"Enter a number: "))
if a < 0:
    raise Exception("Number cannot be negative!")
print(f"Factorial of {a} is {factorialCalculation(a)}")

# v2
def factorialCalculationWithCheck(a):
    if a < 0:
        raise Exception("Number cannot be negative!")
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

a = int(input(f"Enter a number: "))
print(f"Factorial of {a} is {factorialCalculationWithCheck(a)}")

"""Завдання 3
Напишіть програму, яка дає змогу користувачеві заповнити список із клавіатури числами.
Після отримання даних відобразіть на екран меню, яке дозволяє виконати такі операції:
Відображення списку;
Отримання максимального значення у списку;
Отримання мінімального значення у списку;
Відображення значення елемента за індексом, введеним користувачем;
Видалення елемента за індексом, введеним користувачем.
Обробіть виняток, що виникає під час виходу за межі списку (користувач ввів неправильне значення для індексу елемента в списку),
і виведіть повідомлення про помилку."""

def printInfo(myList):
    print()
    print("-List-")
    for ind, item in enumerate(myList):
        print(ind - 1 + 1, '\t', item)
    print('-' * 12, '\n')

user_list = []
while True:
    user_input = input("Enter a number or press \"Enter\" to complete list: ")
    if user_input == "":
        print(f"List complete!")
        break
    else:
        user_list.append(int(user_input))
        pass

if len(user_list) == 0:
    raise Exception("List cannot be empty!")

while True:
    user_choice = input(f"Choice operation from menu:\n"
                        f"1. View list\n"
                        f"2. Max value of list\n"
                        f"3. Min value of list\n"
                        f"4. View value of index\n"
                        f"5. Delete value of index\n"
                        f"6. Exit\n")
    if user_choice == "1":
        printInfo(user_list)
        pass
    elif user_choice == "2":
        print(f"Max value of list:\n{max(user_list)}")
        pass
    elif user_choice == "3":
        print(f"Min value of list:\n{min(user_list)}")
        pass
    elif user_choice == "4":
        user_index = int(input("Enter index for view value: "))
        if user_index not in range(0, len(user_list)):
            raise Exception("Index out of range!")
        print(user_list[user_index])
        pass
    elif user_choice == "5":
        user_index = int(input("Enter index of list to delete: "))
        if user_index not in range(0, len(user_list)):
            raise Exception("Index out of range!")
        user_list.pop(user_index)
        printInfo(user_list)
        pass
    elif user_choice == "6":
        print(f"Have a nice day!")
        user_list.clear()
        break

"""Завдання 4
Реалізуйте третє завдання через функції. Створіть дві версії реалізації функцій:
Перша версія не обробляє винятки всередині функцій. Уся обробка знаходиться зовні;
Друга версія обробляє винятки всередині функцій."""

# v1
def MaxValue(list):
    return max(list)

def MinValue(list):
    return min(list)

def ViewValue(list, index):
    return list[index]

def DeleteValue(list, index):
    list.pop(index)

while True:
    user_input = input("Enter a number or press \"Enter\" to complete list: ")
    if user_input == "":
        print(f"List complete!")
        break
    else:
        user_list.append(int(user_input))
        pass

if len(user_list) == 0:
    raise Exception("List cannot be empty!")

while True:
    user_choice = input(f"Choice operation from menu:\n"
                        f"1. View list\n"
                        f"2. Max value of list\n"
                        f"3. Min value of list\n"
                        f"4. View value of index\n"
                        f"5. Delete value of index\n"
                        f"6. Exit\n")
    if user_choice == "1":
        printInfo(user_list)
        pass
    elif user_choice == "2":
        print(f"Max value of list:\n{MaxValue(user_list)}")
        pass
    elif user_choice == "3":
        print(f"Min value of list:\n{MinValue(user_list)}")
        pass
    elif user_choice == "4":
        user_index = int(input("Enter index for view value: "))
        if user_index not in range(0, len(user_list)):
            raise Exception("Index out of range!")
        print(ViewValue(user_list, user_index))
        pass
    elif user_choice == "5":
        user_index = int(input("Enter index of list to delete: "))
        if user_index not in range(0, len(user_list)):
            raise Exception("Index out of range!")
        DeleteValue(user_list, user_index)
        printInfo(user_list)
        pass
    elif user_choice == "6":
        print(f"Have a nice day!")
        user_list.clear()
        break

# v2
def ViewListCheck(myList):
    if len(myList) == 0:
        raise Exception("List cannot be empty!")
    print()
    print("-List-")
    for ind, item in enumerate(myList):
        print(ind - 1 + 1, '\t', item)
    print('-' * 12, '\n')

def ViewValueCheck(list, index):
    if index not in range(0, len(list)):
        raise Exception("Index out of range!")
    return list[index]

def DeleteValueCheck(list, index):
    if index not in range(0, len(list)):
        raise Exception("Index out of range!")
    list.pop(index)

while True:
    user_input = input("Enter a number or press \"Enter\" to complete list: ")
    if user_input == "":
        print(f"List complete!")
        break
    else:
        user_list.append(int(user_input))
        pass

while True:
    user_choice = input(f"Choice operation from menu:\n"
                        f"1. View list\n"
                        f"2. Max value of list\n"
                        f"3. Min value of list\n"
                        f"4. View value of index\n"
                        f"5. Delete value of index\n"
                        f"6. Exit\n")
    if user_choice == "1":
        ViewListCheck(user_list)
        pass
    elif user_choice == "2":
        print(f"Max value of list:\n{MaxValue(user_list)}")
        pass
    elif user_choice == "3":
        print(f"Min value of list:\n{MinValue(user_list)}")
        pass
    elif user_choice == "4":
        user_index = int(input("Enter index for view value: "))
        print(ViewValueCheck(user_list, user_index))
        pass
    elif user_choice == "5":
        user_index = int(input("Enter index of list to delete: "))
        DeleteValueCheck(user_list, user_index)
        ViewListCheck(user_list)
        pass
    elif user_choice == "6":
        print(f"Have a nice day!")
        user_list.clear()
        break