from random import randint

from HW_m03_p3 import list3

myList = [randint(-10, 10) for _ in range(10)]


def dobInt(myList):
    f = 1
    for i in range(len(myList)):
        f *= myList[i]
    return f


def minInt(myList):
    return min(myList)


def isSimpleInt(a):
    if a % 2 == 0:
        return a == 2
    b = 3
    while b * b <= a and a % b != 0:
        b += 2
    return b * b > a


def simpleInt(myList):
    c = 0
    for i in range(len(myList)):
        if isSimpleInt(myList[i]) == True:
            c += 1
    return c


def delFromList(myList1, a):
    c = 0
    while a in myList1:
        c += 1
        myList1.remove(a)
    return c


def splitLists(list1,list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
    for i in range(len(list2)):
        list3.append(list2[i])
    return list3

def stOfInt(list1,st):
    listSt = []
    for i in range(len(list1)):
        listSt.append(list1[i]**st)
    return listSt


"""Завдання 1
Напишіть функцію для підрахунку добутку елементів списку цілих.
Список передається як параметр. Отриманий результат повертається із функції.
"""

print(f"Добуток цілих зі списку:\n{dobInt(myList)}")
print('-' * 15, '\n')

"""Завдання 2
Напишіть функцію для знаходження мінімуму в списку цілих.
Список передається як параметр. Отриманий результат повертається із функції.
"""

print(f"Мінімальне число зі списку:\n{minInt(myList)}")
print('-' * 15, '\n')

"""Завдання 3
Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
Список передається як параметр. Отриманий результат повертається із функції.
"""

print(f"Кількість простих чисел зі списку:\n{simpleInt(myList)}")
print('-' * 15, '\n')

"""Завдання 4
Напишіть функцію, яка видаляє зі списку цілих певне задане число.
З функції потрібно повернути кількість видалених елементів.
"""

myList1 = [randint(-10, 10) for _ in range(10)]
print(myList1)
d_int = int(input(f"Введіть число для видалення: "))
print(f"Кількість видалених елементів зі списку: \n{delFromList(myList1, d_int)}")
print('-' * 15, '\n')

"""Завдання 5
Напишіть функцію, яка отримує два списки як параметр і повертає список з елементами обох списків.
"""

mylist2 = [randint(-50, 50) for _ in range(10)]
myList3 = [randint(-50, 50) for _ in range(10)]
myList4 = splitLists(mylist2, myList3)
print(f"Новий список: \n{splitLists(mylist2, myList3)}")
print('-' * 15, '\n')

"""Завдання 6
Напишіть функцію, яка підраховує степінь кожного елемента списку цілих.
Значення для степеня, як і список, передається як параметр.
Функція повертає новий список з отриманими результатами.
"""

step = abs(int(input(f"Введіть ступінь числа: ")))
stList = stOfInt(myList, step)
print(f"Список чисел в ступені: \n{stList}")
print('-' * 15)