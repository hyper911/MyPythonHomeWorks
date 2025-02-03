def formatedText():
    p_right = str("Bill Gates").rjust(50)
    print(f"\"Don’t compare yourself with anyone in this world…\n"
          f"\tif you do so, you are insulting yourself.\"\n"
          f"{p_right}")


def evenNumbers(a, b):
    if a > b:
        min_a = b
        min_b = a
    else:
        min_a = a
        min_b = b
    for i in range(min_a, min_b + 1):
        if i % 2 == 0:
            print(i, end=" ")


def printSquare(a, b, c):
    if c == 0:
        c = False
    else:
        c = True

    t = 0
    s = " "

    if c == True:
        for i in range(a):
            print(f"{b * a}")
    else:
        for i in range(a):
            if i == 0 or i == (a - 1):
                print(f"{b * a}")
            else:
                print(f"{b}{s * (a - 2)}{b}")


def minNumbers(*pNumbers):
    print(f"Мінімальне число: {min(*pNumbers)}")


def dobNumbers(a, b):
    if a > b:
        min_a = b
        min_b = a
    else:
        min_a = a
        min_b = b

    d = 1

    for i in range(min_a, min_b + 1):
        d *= i
    print(f"Добуток чисел діапазону: {d}")


def countOfNumbers(a):
    print(f"Кількість цифр в числі: {len(str(a))}")


def palindromNumber(a):
    l = len(str(a))
    if l % 2 == 0:
        p1 = str(a)[:(l//2)]
        p2 = str(a)[(l//2):]
        if p1 == p2[::-1]:
            return True
        else:
            return False
    else:
        return None

"""Завдання 1
Напишіть функцію, яка виводить на екран форматований текст, наведений нижче:
“Don’t compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                        Bill Gates
"""

formatedText()
print('-' * 15)

"""Завдання 2
Напишіть функцію, яка приймає два числа як параметр і відображає усі парні числа між ними.
"""

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
evenNumbers(a, b)
print('\n', '-' * 15)

"""Завдання 3
Напишіть функцію, яка відображає порожній або заповнений квадрат із певним символом.
Функція приймає в якості параметрів довжину сторони квадрата, символ та змінну логічного типу: 
■ якщо вона дорівнює True, квадрат заповнений;
■ якщо False, квадрат порожній.
"""

a = int(input("Введіть довжину сторони квадрату: "))
b = input("Введіть символ: ")
c = int(input("Введіть 0 або 1: "))
printSquare(a, b, c)
print('-' * 15)

"""Завдання 4
Напишіть функцію, яка повертає мінімальне з п’яти чисел. 
Числа передаються як параметри.
"""
a = int(input("Введіть перше число: "))
b = int(input("Введіть друга число: "))
c = int(input("Введіть третє число: "))
d = int(input("Введіть четверте число: "))
e = int(input("Введіть п'яте число: "))
minNumbers(a, b, c, d, e)
print('-' * 15)

"""
Завдання 5
Напишіть функцію, яка повертає добуток чисел у зазначеному діапазоні. Межі діапазону передаються як параметри. 
Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.
"""

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
dobNumbers(a, b)
print('-' * 15)

"""Завдання 6
Напишіть функцію, яка підраховує кількість цифр у числі. 
Число передається як параметр. Поверніть з функції отриману кількість цифр.
Наприклад, якщо передали 3456, кількість цифр буде 4.
"""

a = int(input("Введіть число: "))
countOfNumbers(a)
print('-' * 15)

"""Завдання 7
Напишіть функцію, яка перевіряє число на паліндром. 
Число передається як параметр. Якщо число є паліндромом, поверніть з функції true, якщо ні — false.
«Паліндром» — це число, в якому перша частина цифр дорівнює другій перевернутій частини цифр.
Наприклад, 123321 — паліндром (перша частина 123, друга 321, яка після перевороту стає 123),
546645 — паліндром, а 421987 — не паліндром.
"""

a = int(input("Введіть число: "))
b = palindromNumber(a)
if b == True or b == False:
    print(b)
else:
    print(f"Число містить не парну кількість цифр!")
