from random import randint


def sumOfIntList(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    print(f"Сумма всіх чисел у списку: {s}")


def maxOfIntList(*args):
    print(f"Максимум зі списку: {max(args)}")


def countOfIntList(*args):
    c_even = c_odd = c_dod = c_vid = 0
    for i in range(len(args)):
        if args[i] % 2 == 0:
            c_even += 1
        elif not args[i] % 2 == 0:
            c_odd += 1
        if args[i] > 0:
            c_dod += 1
        else:
            c_vid += 1
    print(
        f"Кількість парних: {c_even}\nКількість непарних: {c_odd}\nКількість додатних: {c_dod}\nКількість від'ємних: {c_vid}")


def reverseIntList(*args):
    print(f"Інвертований список: \n{args[::-1]}")


def findOfIntList(*args):
    f = args[-1]
    c_f = args.count(f) - 1
    if c_f > 0:
        print(f"Число {f} знайдено у списку {c_f} раз.")
    else:
        print(f"Число {f} не знайдено у списку!")


def factorialOfList(*args):
    fList = []

    for i in args:
        if i >= 0:
            f = 1
            for n in range(1, i+1):
                f = f * n
            fList.append(f)

    return fList


def printList(myList):
    for index, elem in enumerate(myList):
        print("{}: {}".format(index + 1, elem))


"""Завдання 1
Напишіть функцію, яка підраховує суму елементів
списку цілих. Список передається як параметр.
"""

intList = [randint(-50, 100) for _ in range(20)]
print()
sumOfIntList(*intList)
print('-' * 20, '\n')

"""Завдання 2
Напишіть функцію, яка знаходить максимум у списку
цілих. Список передається як параметр.
"""

intList = [randint(-50, 100) for _ in range(20)]
maxOfIntList(*intList)
print('-' * 20, '\n')

"""
Завдання 3
Напишіть функцію, яка визначає кількість парних,
непарних, додатних, від’ємних елементів списку цілих.
Список передається як параметр.
"""

intList = [randint(-50, 100) for _ in range(20)]
countOfIntList(*intList)
print('-' * 20, '\n')

"""Завдання 4
Напишіть функцію, що перевертає вміст списку цілих.
"""

intList = [randint(-50, 100) for _ in range(20)]
reverseIntList(*intList)
print('-' * 20, '\n')

"""Завдання 5
Напишіть функцію, яка шукає певне число в списку цілих.
"""

intList = [randint(-50, 100) for _ in range(20)]
intFind = randint(-50, 100)
findOfIntList(*intList, intFind)
print('-' * 20, '\n')

"""Завдання 6
Напишіть функцію, яка підраховує факторіал кожного елемента списку цілих.
Функція повертає новий список, що містить отримані факторіали.
"""

intList = [randint(-10, 10) for _ in range(20)]
nList = factorialOfList(*intList)
print(f"Список факторіалів: ")
printList(nList)
print('-' * 20)
