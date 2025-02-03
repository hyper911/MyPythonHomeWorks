from random import randint

"""Завдання 1
Створіть функцію, яка повертає всі парні числа в діапазоні. Функція приймає початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.
"""


def evenNumber(a, b):
    if b > a:
        min_a = b
        min_b = a
    else:
        min_a = a
        min_b = b
    listGen = [randint(-100, 100) for _ in range(25)]
    listEven = list(filter(lambda x: x % 2 == 0, listGen))
    return listEven


print(f"\n"
      f"Парні числа діапазону:\n"
      f"{evenNumber(randint(-100, 100), randint(-100, 100))}")
print('-' * 20)
