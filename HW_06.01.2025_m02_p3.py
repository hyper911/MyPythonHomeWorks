"""Завдання 1
Користувач вводить з клавіатури число від 1 до 100. Якщо
число кратне 3 (ділиться на 3 без остачі), виведіть слово «Fizz».
Якщо число кратне 5, виведіть слово «Buzz». Якщо число
кратне 3 та 5, потрібно вивести «Fizz Buzz». Якщо число не
кратне ні 3, ані 5, виведіть тільки число.
Якщо користувач ввів значення не в діапазоні від 1 до
100, виведіть повідомлення про помилку."""


def numberToThree(user_number):
    if user_number % 3 == 0 and user_number % 5 == 0:
        return f"Fizz Buzz"
    elif user_number % 3 == 0:
        return f"Fizz"
    elif user_number % 5 == 0:
        return f"Buzz"


while True:
    user_input = int(input("Input a number from 1 to 100: "))
    if user_input not in range(1, 100):
        print("Your number not in ranfge 1 to 100!")
        continue
    else:
        print(numberToThree(user_input))
        break

"""Завдання 2
Напишіть програму, яка на вибір користувача піднесе 
введене ним число до степеня від нульового до сьомого 
включно."""


def printInfo(myList):
    print()
    for ind, item in enumerate(myList):
        print(ind, ':', item)
    print('-' * 12, '\n')


def numberToStepen(user_number):
    lst = []
    lst.clear()

    for i in range(0, 8):
        lst.append(user_number ** i)
    printInfo(lst)


user_number = int(input("Input a number: "))
numberToStepen(user_number)

"""Завдання 3
Напишіть програму підрахунку вартості розмови для 
різних мобільних операторів. Користувач вводить вартість 
розмови та вибирає, з якого на який оператор він дзвонить. 
Виведіть вартість розмови на екран.
"""


def vartistRozmovy(user_cost, op1, op2):
    if op1 == op2:
        print(f"Call cost: {user_cost}")
    else:
        print(f"Call cost: {(user_cost * op1) + (user_cost * op2)}")


operators_list = {"Kyivstar": 1.0,
                  "Life": 1.2,
                  "Vodafone": 1.15,
                  "Lycamobile": 2.0}

user_cost = int(input("input cost of call: "))
while True:
    user_op1 = input(f"Choose operator from call: \n"
                     f"1. Kyivstar \n"
                     f"2. Life \n"
                     f"3. Vodafone \n"
                     f"4. Lycamobile \n")
    if user_op1.startswith("1"):
        op1 = operators_list["Kyivstar"]
        break
    elif user_op1.startswith("2"):
        op1 = operators_list["Life"]
        break
    elif user_op1.startswith("3"):
        op1 = operators_list["Vodafone"]
        break
    elif user_op1.startswith("4"):
        op1 = operators_list["Lycamobile"]
        break
    else:
        print("invalid input")

while True:
    user_op2 = input(f"Choose operator to call: \n"
                     f"1. Kyivstar \n"
                     f"2. Life \n"
                     f"3. Vodafone \n"
                     f"4. Lycamobile \n")
    if user_op2.startswith("1"):
        op2 = operators_list["Kyivstar"]
        break
    elif user_op2.startswith("2"):
        op2 = operators_list["Life"]
        break
    elif user_op2.startswith("3"):
        op2 = operators_list["Vodafone"]
        break
    elif user_op2.startswith("4"):
        op2 = operators_list["Lycamobile"]
        break
    else:
        print("invalid input")

vartistRozmovy(user_cost, op1, op2)

"""Завдання 4
Зарплата менеджера становить 200$ + відсоток від продажу: 
продаж до 500$ – 3%, 500 –1000$ – 5%, понад 1000$ – 8%.
Користувач вводить з клавіатури рівень продажу для трьох менеджерів.
Визначте їхню зарплату, а також найкращого менеджера, 
нарахуйте йому премію 200$ та виведіть підсумки на екран."""


def zarplataManagers(manager_dict, zp=200):
    if manager_dict == {}:
        print(f"Not managers at list!")
    else:
        max_sales = max(manager_dict.values())
        for key, value in manager_dict.items():
            if value == max_sales:
                best_manager = key
            if value < 500:
                manager_dict[key] = zp + value * 0.03
            elif value > 500 and value < 1000:
                manager_dict[key] = zp + value * 0.05
            else:
                manager_dict[key] = zp + value * 0.08
            print(f"{key} : {manager_dict[key]}")
        print(f"Best manager: {best_manager}")


manager_lst = ["Manager_1", "Manager_2", "Manager_3"]
manager_dict = {}

for i in manager_lst:
    user_sales_manager = int(input(f"Input sales amount for {i}: "))
    manager_dict.update({i: user_sales_manager})

zarplataManagers(manager_dict)
