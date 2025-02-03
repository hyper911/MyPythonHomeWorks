from random import randint


def splitLists(list1, list2):
    myList = list1 + list2
    if len(list1) != 0 and len(list2) != 0:
        myList.sort()
        return myList


def deleteRepeated(listForCheck):
    mylist = listForCheck
    u_values = set(listForCheck)
    mylist.clear()
    for i in u_values:
        mylist.append(i)
    mylist.sort()
    return mylist


def findShared(list1, list2):
    myList = []
    startIndex = 0

    for i in list1:
        if i in list2:
            myList.append(i)
    myList.sort()
    listOfShared = deleteRepeated(myList)
    return listOfShared


"""
Завдання
Два списки цілих заповнюються випадковими числами.
Сформуйте третій список, який містить:
■ елементи обох списків;
■ елементи обох списків без повторень;
■ елементи, спільні для двох списків;
■ тільки унікальні елементи кожного зі списків;
■ тільки мінімальне та максимальне значення кожного зі
списків.
"""

list1 = [randint(-50, 50) for _ in range(20)]
list2 = [randint(-50, 50) for _ in range(20)]
list3 = splitLists(list1, list2)

print(f"\nЕлементи обох списків:\n{list3}")

print(f"\nЕлементи обох списків без повторень:\n{deleteRepeated(list3)}")

list4 = findShared(list1, list2)
if len(list4) > 0:
    print(f"\nЕлементи, спільні для двох списків:\n{list4}")
else:
    print(f"\nСпільні елементи відсутні!")

print(f"\nУнікальні для кожного зі списків:\n{deleteRepeated(list1)}\n{deleteRepeated(list2)}")

print(
    f"\nМінімальне значення списку 1: {min(list1)}\nМаксимальне значення списку 1: {max(list1)}\nМінімальне значення списку 2: {min(list2)}\nМаксимальне значення списку 2: {max(list2)}")
