from random import randint


def findFruit(lisfOfFind, fruitName):
    if lisfOfFind.count(fruitName) > 0:
        return lisfOfFind.count(fruitName)
    else:
        return 0


def findFruitSubLevel(lisfOfFind, fruitName):
    listOfFound = [0, 0]
    cFind = 0
    for i in lisfOfFind:
        if fruitName in i and len(fruitName) <= len(i):
            cFind += 1
            listOfFound[0] = cFind
        else:
            listOfFound[0] = 0

    if lisfOfFind.count(fruitName) > 0:
        listOfFound[1] = (lisfOfFind.count(fruitName))
    else:
        listOfFound[1] = 0

    return listOfFound


def replaceCarManufacturer(listOfFind, manName, replaceName):
    listofFound = list(listOfFind)

    if manName == "":
        carName = input("Введіть нззву виробника авто (англійською): ").strip()

    if replaceName == "":
        replaceName = input("Введіть слово для заміни: ").strip()

    for i in range(len(listofFound)):
        if manName == listofFound[i]:
            listofFound[i] = replaceName

    del listOfFind
    carTuple = tuple(listofFound)

    return carTuple


def statOfTuple(listOfFind):
    listOfWords = []
    listOfStat = []

    for i in range(len(listOfFind)):
        a = str(abs(listOfFind[i]))
        listOfWords.append(a)
    listOfWords.sort()

    x_min = min(listOfFind)
    x_max = max(listOfFind)
    if x_min > x_max:
        max_len = len(str(x_min))
    else:
        max_len = len(str(x_max))

    for startNumber in range(max_len + 1):
        count = 0
        listOfNumbers = [0, 0]
        for item in listOfWords:
            if len(item) == startNumber:
                count += 1
                listOfNumbers[0] = startNumber
                listOfNumbers[1] = count
        if listOfNumbers[0] != 0 and listOfNumbers[1] != 0:
            listOfStat.append(listOfNumbers)

    for i in range(len(listOfStat)):
        word = numberToWord(listOfStat[i][0])
        listOfStat[i][0] = word

    return listOfStat


def printListOfElements(myList):
    for i in range(len(myList)):
        print(f"{myList[i][0]} - {myList[i][1]} {wordInCase(myList[i][1])}")


def wordInCase(number):
    numToStr = str(number)

    if len(numToStr) > 1:
        lastNumber = int(numToStr[len(numToStr) - 1])
    else:
        lastNumber = number

    if number == 0 or lastNumber == 0:
        word = "елементів"
    elif number == 1 or lastNumber == 1:
        word = "елемент"
    elif (number > 1 and number < 5) or (lastNumber > 1 and lastNumber < 5):
        word = "елементи"
    else:
        word = "елементів"

    return word


def numberToWord(number):
    listOfWord = ["Одна цифра", "Дві цифри", "Три цифри", "Чотири цифри", "П'ять цифр", "Шість цифр", "Сім цифр",
                  "Вісім цифр", "Дев'ять цифр", "Десять цифр"]

    numToWord = listOfWord[number - 1]

    return numToWord


"""
Завдання 1
Користувач вводить з клавіатури назву фрукта. Виведіть на екран кількість фруктів,
що містяться в кортежі як елемент.
"""

tupleFruit = tuple(('banana', 'apple', 'orange', 'banana-mango', 'mango', 'strawberry-banana'))
fruitName = input("Введіть назву фрукту англійською: ").strip().lower()
fruitFind = findFruit(tupleFruit, fruitName)

if fruitFind > 0:
    print(f"\nУ кортежі фрукт {fruitName} зустрічається {fruitFind} раз(ів)")
else:
    print(f"\nУ кортежі фрукт {fruitName} не зустрічається!")
print('-' * 20, '\n')

"""
Завдання 2
Додайте до першого завдання підрахунок кількості, коли назва фрукта є частиною елемента.
Наприклад, banana, apple, bananamango, mango, strawberry-banana. 
У приведеному прикладі banana зустрічається три рази.
"""

fruitName = input("Введіть назву фрукту англійською: ").strip().lower()
fruitFind = findFruitSubLevel(tupleFruit, fruitName)

if fruitFind[0] > 0:
    print(f"У кортежі фрукт {fruitName} є частиною назви {fruitFind[0]} елементу(ів)")
else:
    print(f"У кортежі фрукт {fruitName} не зустрічається!")
if fruitFind[1] > 0:
    print(f"У кортежі фрукт {fruitName} зустрічається {fruitFind[1]} раз(ів)")
else:
    print(f"У кортежі фрукт {fruitName} не зустрічається!")
print('-' * 20, '\n')

"""Завдання 3
Маємо кортеж з назвами автовиробників (назва виробника може зустрічатися від 0 до N разів).
Користувач вводить з клавіатури назву виробника та слово для заміни.
Замініть в кортежі усі елементи з цією назвою на слово для заміни.
Збіг за назвою має бути повним.
"""

carTuple = (('Chevrolet', 'Mazda', 'Mazda', 'Volvo', 'Mercedes-Benz', 'Volvo', 'KIA', 'MAN'))
carName = input("Введіть нззву виробника авто (англійською): ").strip()
replaceName = input("Введіть слово для заміни: ").strip()
carTuple = replaceCarManufacturer(carTuple, carName, replaceName)
print(carTuple)
print('-' * 20, '\n')

"""Завдання 4
Маємо кортеж з цілими числами. Виведіть статистику за кількістю цифр в елементах кортежу.
Наприклад:
    Одна цифра — 3 елементи
    Дві цифри — 4 елементи
    Три цифри — 5 елементів
"""

numbersTuple = ([randint(-50000, 50000) for _ in range(100)])
statsNumber = statOfTuple(numbersTuple)
print("Статистика елементів в кортежі:")
printListOfElements(statsNumber)
