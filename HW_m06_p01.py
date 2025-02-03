from random import randint


def duplicateOfInt(t1, t2, t3):
    c = set()
    for i in t1:
        if i in t2 and i in t3:
            c.add(i)
    if len(c) == 0:
        return 0
    else:
        return c


def uniqueOfInt(t1, t2, t3):
    a = set()
    b = set()
    c = set()
    d = []
    for i in t1:
        a.add(i)
    for i in t2:
        b.add(i)
    for i in t3:
        c.add(i)
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)
    d.append(a)
    d.append(b)
    d.append(c)

    return d


def uniqAndIndexOfInt(t1, t2, t3):
    c = set()
    for i in range(len(t1)):
        if (t1[i] == t2[i] == t3[i]):
            c.add(t1[i])
    if len(c) == 0:
        return 0
    else:
        return c


"""Завдання 1
Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.
"""

myTuple1 = tuple(randint(-50, 50) for _ in range(30))
myTuple2 = tuple(randint(-50, 50) for _ in range(30))
myTuple3 = tuple(randint(-50, 50) for _ in range(30))
d = duplicateOfInt(myTuple1, myTuple2, myTuple3)
print(f"\nОднакові числа в кортежах:")
if d != 0:
    for item in d:
        print(item, end=" ")
    print()
else:
    print(f"відсутні!")
print('-' * 15)

"""Завдання 2
Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.
"""

d = uniqueOfInt(myTuple1, myTuple2, myTuple3)
print(f"\nУнікальні числа кортежів:")
for list in d:
    print(list)
print('-' * 15)

"""Завдання 3
Маємо три кортежі цілих чисел.
Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції.
"""

d = uniqAndIndexOfInt(myTuple1, myTuple2, myTuple3)
print(f"\nОднакові числа на однаковій позиції в кортежах:")
if d != 0:
    for item in d:
        print(item, end=" ")
    print()
else:
    print(f"відсутні!")
print('-' * 15)
