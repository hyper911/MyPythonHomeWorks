from random import randint

"""Завдання 1
Напишіть рекурсивну функцію знаходження степені числа."""

def stOfNumber(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    return a * stOfNumber(a, b - 1)

a = int(input("Введіть число: "))
b = int(input("Введіть ступень числа: "))
print(stOfNumber(a, b))

"""Завдання 2
Напишіть рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
Користувач вводить a та b. Покажіть приклад роботи функції."""

def summOfNumbers(a, b):
    if a > b:
        return 0
    return b + summOfNumbers(a, b - 1)

a = int(input("Введіть перше число діапазону: "))
b = int(input("Введіть друге число діапазону: "))
print(summOfNumbers(a, b))

"""Завдання 3
Напишіть рекурсивну функцію, яка виводить в рядок N зірочок,
число N задає користувач. Покажіть приклад роботи функції."""

def printOfSymbol(c):
    if c > 0:
        print('*', end = '')
        printOfSymbol(c - 1)
    else:
        print()

c = int(input("Введіть кількість зірочок: "))
print(printOfSymbol(c))

"""Завдання 4
Створіть гру «Хрестики-Нулики»."""

def checkResult(list1, list2, list3):
    if ((list1.count('x') == 3 or list2.count('x') == 3 or list3.count('x') == 3)
            or (list1[0] == list2[0] == list3[0] == 'x')
            or (list1[1] == list2[1] == list3[1] == 'x')
            or (list1[2] == list2[2] == list3[2] == 'x')
            or (list1[0] == list2[1] == list3[2] == 'x')
            or (list1[2] == list2[1] == list3[0] == 'x')):
        print('\n', "Перший гравець переміг!", '\n', '-' * 25, sep = '')
        return True
    elif ((list1.count('0') == 3 or list2.count('0') == 3 or list3.count('0') == 3)
          or (list1[0] == list2[0] == list3[0] == '0')
          or (list1[1] == list2[1] == list3[1] == '0')
          or (list1[2] == list2[2] == list3[2] == '0')
          or (list1[0] == list2[1] == list3[2] == '0')
          or (list1[2] == list2[1] == list3[0] == '0')):
        print('\n', "Другий гравець переміг!", '\n', '-' * 25, sep = '')
        return True
    elif list1.count(' ') == 0 and list2.count(' ') == 0 and list3.count(' ') == 0:
        print('\n', "Нічия! Перемогла дружба!", '\n', '-' * 25, sep = '')
        return True
    else:
        return False

def checkInp(curList, indInp, symbInp):
    if curList[indInp] == 'x' or curList[indInp] == '0':
        return False
    else:
        curList[indInp] = symbInp
        return True

user_choice = input(f"\n{("-=Гра хрестики-нулики=-").rjust(25)}\n"
                    f"(Перший гравець грає хрестиком, другий гравець - нуликом)\n"
                    f"{'-' * 20}\n"
                    f"1. Почати гру.\n"
                    f"2. Вихід.\n"
                    f"Введіть цифру меню: ")
if user_choice.startswith("1"):
    list1 = [" ", " ", " "]
    list2 = [" ", " ", " "]
    list3 = [" ", " ", " "]
    inpPlayer = 1
    print('\n', list1, '\n', list2, '\n', list3, sep = "")
    while True:
        if inpPlayer % 2 != 0:
            p1_v = input(f"\n{("-Перший гравець (х)-").rjust(25)}\n"
                         f"Оберіть горизонтальний блок з трьох клітинок:\n"
                         f"1. Верхній.\n"
                         f"2. Середній.\n"
                         f"3. Нижній.\n"
                         f"Введіть цифру меню: ")
            if p1_v.startswith("1"):
                paramList = list1
            elif p1_v.startswith("2"):
                paramList = list2
            elif p1_v.startswith("3"):
                paramList = list3
            else:
                print(f"Не вірний номер меню!")
                pass
            p1_h = input(f"\n{("-Перший гравець (х)-").rjust(25)}\n"
                         f"Оберіть позицію:\n"
                         f"1. Зліва.\n"
                         f"2. Посередині.\n"
                         f"3. Справа.\n"
                         f"Введіть цифру меню: ")
            if p1_h.startswith("1"):
                paramInd = 0
            elif p1_h.startswith("2"):
                paramInd = 1
            elif p1_h.startswith("3"):
                paramInd = 2
            else:
                print(f"Не вірний номер меню!")
                pass
            if checkInp(paramList, paramInd, 'x'):
                print('\n', list1, '\n', list2, '\n', list3, sep = "")
                if checkResult(list1, list2, list3) == False:
                    inpPlayer += 1
                else:
                    print("Гра закінчилася!")
                    break
            else:
                print('\n', "Позиція вже зайнята!")
                print('\n', list1, '\n', list2, '\n', list3, sep = "")
                pass
        else:
            p2_v = input(f"\n{("--Другий гравець (0)--").rjust(25)}\n"
                         f"Оберіть горизонтальний блок з трьох клітинок:\n"
                         f"1. Верхній.\n"
                         f"2. Середній.\n"
                         f"3. Нижній.\n"
                         f"Введіть цифру меню: ")
            if p2_v.startswith("1"):
                paramList = list1
            elif p2_v.startswith("2"):
                paramList = list2
            elif p2_v.startswith("3"):
                paramList = list3
            else:
                print(f"Не вірний номер меню!")
                pass
            p2_h = input(f"\n{("--Другий гравець (0)--").rjust(25)}\n"
                         f"Оберіть позицію:\n"
                         f"1. Зліва.\n"
                         f"2. Посередині.\n"
                         f"3. Справа.\n"
                         f"Введіть цифру меню: ")
            if p2_h.startswith("1"):
                paramInd = 0
            elif p2_h.startswith("2"):
                paramInd = 1
            elif p2_h.startswith("3"):
                paramInd = 2
            else:
                print(f"Не вірний номер меню!")
                pass
            if checkInp(paramList, paramInd, '0'):
                print('\n', list1, '\n', list2, '\n', list3, sep = "")
                if checkResult(list1, list2, list3) == False:
                    inpPlayer += 1
                else:
                    print("Гра закінчилася!")
                    break
            else:
                print('\n', "Позиція вже зайнята!")
                print('\n', list1, '\n', list2, '\n', list3, sep = "")
                pass
elif user_choice.startswith("2"):
    print("Гарного дня!")


"""Завдання 5
Напишіть рекурсивну функцію, яка приймає список із 100 цілих чисел, отриманих випадковим чином,
і знаходить позицію, з якої починається послідовність з 10 чисел, сума яких мінімальна."""

def sumOfMinimalNumbers(myList, listofInd, c = 1):
    start_index = 0
    end_index = 10
    if len(myList) == 10:
        return sum(myList)
    s1 = sum(myList[start_index:end_index])
    s2 = sumOfMinimalNumbers(myList[start_index + 1:], listofInd, c + 1)
    if s1 < s2:
        if listOfInd == []:
            listOfInd.append(s1)
            listOfInd.append(c)
        elif listOfInd[0] != s1:
            listOfInd[0] = s1
            listOfInd[1] = c
        return s1
    else:
        if listOfInd == []:
            listOfInd.append(s2)
            listOfInd.append(c)
        elif listOfInd[0] != s2:
            listOfInd[0] = s2
            listOfInd[1] = c
        return s2

myList = [randint(-100, 100) for _ in range(100)]
listOfInd = []
minSum = sumOfMinimalNumbers(myList, listOfInd)
maxIteration = len(myList) - 10
if listOfInd[1] == maxIteration:
    indexOfStart = listOfInd[1]
else:
    indexOfStart = listOfInd[1] - 1
print(f"\nМінімальна сума послідовності:\t{listOfInd[0]}\nІндекс початку послідовності:\t{indexOfStart}")

"""Завдання 6
Напишіть функцію, яка приймає дві дати (тобто функція приймає шість параметрів)
та обчислює різницю в днях між цими датами. Для вирішення цього завдання напишіть також функцію,
яка визначає, чи є рік високосним."""

def riznyucyaDat(*params):
    data1 = [params[0], params[1], params[2]]
    data2 = [params[3], params[4], params[5]]
    listOfDays = params[6]

    if data2 == data1:
        return 0
    elif data2[0] >= data1[0] and data2[1] >= data1[1]:
        c_start_year_high = highDataYear(data1[0])
        c_end_year_high = highDataYear(data2[0])
        h = 0

        for i in range(data1[0], data2[0] + 1):
            if highDataYear(i):
                h += 1
        if data2[0] == data1[0]:
            c_days_of_years = 0
        else:
            c_days_of_years = (h * 366) + (data2[0] - data1[0] - h) * 365

        if data1[1] == 1:
            c_start_day = data1[2]
        elif not c_start_year_high and data1[1] > 1:
            c_start_day = sum(listOfDays[0:data1[1] - 1]) + data1[2]
        elif c_start_year_high and data1[1] > 1:
            c_start_day = sum(listOfDays[0:data1[1] - 1]) + data1[2]
        elif c_start_year_high and data1[1] > 2:
            c_start_day = sum(listOfDays[0:data1[1] - 1]) + data1[2] + 1

        if data2[1] == 1:
            c_end_day = data2[2] + c_days_of_years
        elif not c_end_year_high and data2[1] > 1:
            c_end_day = sum(listOfDays[0:data2[1] - 1]) + data2[2] + c_days_of_years
        elif c_end_year_high and data2[1] > 1:
            c_end_day = sum(listOfDays[0:data2[1] - 1]) + data2[2] + c_days_of_years
        elif c_end_year_high and data2[1] > 2:
            c_end_day = sum(listOfDays[0:data2[1] - 1]) + data2[2] + 1 + c_days_of_years

        r_dat = c_end_day - c_start_day
        return r_dat

def highDataYear(myYear):
    return myYear % 4 == 0

listOfCalendar = [31] * 12
listOfCalendar[1] = 28
listOfCalendar[3] = listOfCalendar[5] = listOfCalendar[8] = listOfCalendar[10] = 30
year1 = int(input(f"Введіть рік початку періоду : "))
month1 = int(input(f"Введіть місяць початку періоду : "))
day1 = int(input(f"Введіть день початку періоду : "))
year2 = int(input(f"Введіть рік закінчення періоду : "))
month2 = int(input(f"Введіть місяць закінчення періоду : "))
day2 = int(input(f"Введіть день закінчення періоду : "))
print(f"Різниця між датами в днях: {riznyucyaDat(year1, month1, day1, year2, month2, day2, listOfCalendar)}")
