from random import randint


def myBubleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp


def InsertionSort(myList):
    n = len(myList)
    for i in range(1, n):
        tmp_list = myList[i]
        j = i

        while j > 0 and myList[j - 1] > tmp_list:
            myList[j] = myList[j - 1]
            j -= 1

        myList[j] = tmp_list


def printList(myList):
    for index, elem in enumerate(myList):  # розбиває на словник
        print("елемент {}: {}".format(index + 1, elem))


def MergeSort(myList):
    if len(myList) > 1:
        m = len(myList) // 2
        leftPart = myList[:m]
        rightPart = myList[m:]

        MergeSort(leftPart)
        MergeSort(rightPart)

        i = j = k = 0

        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                myList[k] = leftPart[i]
                i += 1
            else:
                myList[k] = rightPart[j]
                j += 1
            k += 1

        while i < len(leftPart):
            myList[k] = leftPart[i]
            i += 1
            k += 1
        while j < len(rightPart):
            myList[k] = rightPart[j]
            j += 1
            k += 1


def SortWithReverse(myList, rev):
    if len(myList) > 1:
        m = len(myList) // 2
        leftPart = myList[:m]
        rightPart = myList[m:]
        tmp_list = []

        if rev == "left":
            leftPart.sort(reverse=True)
            rightPart.sort(reverse=False)
        elif rev == "right":
            leftPart.sort(reverse=False)
            rightPart.sort(reverse=True)
        else:
            leftPart.sort(reverse=False)
            rightPart.sort(reverse=False)

        for i in range(len(leftPart)):
            tmp_list.append(leftPart[i])

        for i in range(len(rightPart)):
            tmp_list.append(rightPart[i])

        for c in range(len(tmp_list)):
            myList[c] = tmp_list[c]


"""Завдання 1
Напишіть програму для сортування списку цілих
чисел методом бульбашкового сортування."""

numbers2 = []
for i in range(10):
    numbers2.append((randint(0, 100)))

myBubleSort(numbers2)
print("Відсортований список: ")
printList(numbers2)
print('-' * 20, end="\n\n")

"""Завдання 2
Напишіть програму для сортування списку цілих
чисел методом вставок."""

numbers3 = []
for i in range(10):
    numbers3.append((randint(0, 100)))

InsertionSort(numbers3)
print("Відсортований список: ")
printList(numbers3)
print('-' * 20, end="\n\n")

"""Завдання 3
Маємо список цілих. Відсортуйте першу половину
списку за спаданням, другу половину — за зростанням."""

numbers4 = []
for i in range(11):
    numbers4.append((randint(0, 100)))

print("Відсортований список: ")
SortWithReverse(numbers4, rev="left")
printList(numbers4)
print('-' * 20, end="\n\n")

"""Завдання 4
Напишіть програму для сортування списку цілих
чисел методом злиття."""

numbers5 = []
for i in range(10):
    numbers5.append((randint(0, 100)))

MergeSort(numbers5)
print("Відсортований список: ")
printList(numbers5)
print('-' * 20, end="\n\n")
