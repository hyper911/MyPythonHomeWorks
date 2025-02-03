from time import time

"""
Завдання 4
Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх чисел.
Відобразіть на екран кількість секунд і всі парні числа від 0 до 100 000.
"""

def simpleDecor(myFunction):
    def simpleWrapper():
        start = time()
        myFunction()
        end = time()
        time_to_result = end - start
        print(f"Time for operation: {round(time_to_result, 2)}")

    return simpleWrapper

@simpleDecor
def EvenNumbers():
    l_en = list(filter(lambda x: x % 2 == 0, range(0, 100000 + 1)))
    print(l_en)

@simpleDecor
def EvenNumbersWithParams():
    l_en = list(filter(lambda x: x % 2 == 0, range(int(input(f"Start diapason: ")), int(input(f"End diapason: ")) + 1)))
    print(l_en)

EvenNumbers()
print('-' * 20)

"""Завдання 5
Додайте до четвертого завдання можливість передавати межі діапазону для пошуку всіх парних чисел."""

EvenNumbersWithParams()
