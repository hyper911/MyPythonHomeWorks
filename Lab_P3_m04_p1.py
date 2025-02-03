def listText(text):
    tmp_txt = text

    razd = " "
    start_index = 0
    end_index = 0
    f_iter = tmp_txt.count(" ")
    i = 1
    space = a = 0
    last_word = tmp_txt[len(tmp_txt) - 4:]
    txt_list = []
    str_end_temp = '"'
    f_str_temp = s_str_temp = t_str_temp = ""

    while i < f_iter + 1:
        tmp_find = tmp_txt[start_index:].find(razd) + 1
        space += tmp_find
        end_index = space
        txt_list.append(tmp_txt[start_index:end_index - 1])
        start_index += tmp_find
        i += 1
    else:
        txt_list.append(last_word)
        pass

    first_str_elem = txt_list[:7]
    third_str_elem = txt_list[len(txt_list) - 2:]
    second_str_elem = txt_list[len(first_str_elem):len(txt_list) - len(third_str_elem)]

    for a in range(len(first_str_elem)):
        f_str_temp += first_str_elem[a] + " "
        f_temp = f_str_temp.rstrip()

    for a in range(len(second_str_elem)):
        s_str_temp += second_str_elem[a] + " "
        s_temp = s_str_temp.rstrip()

    for a in range(len(third_str_elem)):
        t_str_temp += third_str_elem[a] + " "
        t_temp = t_str_temp.rjust(39)

    tmp_txt = f"{str_end_temp}{f_temp}\n{s_temp}{str_end_temp}\n{t_temp}"

    return tmp_txt


def viewOddNumbers(minInt, maxInt):
    if maxInt < minInt:
        x_min = maxInt
        x_max = minInt
    else:
        x_min = minInt
        x_max = maxInt

    print(f"Непарні числа:")
    for i in range(x_min, x_max + 1):
        if not i % 2 == 0:
            print(f"{i}")


def printLine(dovjina, napryam, simvol):
    if napryam == 1:
        print("Горизонтальна лінія:")
        print(f"{simvol * dovjina}")
    elif napryam == 2:
        print("Вертикальна лінія:")
        for i in range(dovjina):
            print(f"{simvol}")
    else:
        print("Не вірно вказаний напрямок!")


def maxFromFour(x1, x2, x3, x4):
    print(f"Максимальне число з чотирьох: {max(x1, x2, x3, x4)}")


def sumFromDiapason(x, y):
    if y < x:
        x_min = y
        x_max = x
    else:
        x_min = x
        x_max = y

    sum_xy = 0

    for i in range(x_min, x_max + 1):
        sum_xy += i

    print(f"Сумма чисел діапазону: {sum_xy}")


def provPrimeNumber(x):
    z = "Число має бути більше одиниці і не дорівнювати нулю!"
    if x > 1 and x != 0:
        if x % 2 == 0:
            return x == 2
        y = 3
        while y * y <= x and x % y != 0:
            y += 2
        return y * y > x
    else:
        return z


def provLuckNumber(x):
    z = "Число не шестизначне!"
    if len(x) == 6:
        f_part = x[:3]
        s_part = x[3:]
        s_f_part = s_s_part = 0

        for i in range(len(f_part)):
            s_f_part += int(f_part[i])

        for i in range(len(s_part)):
            s_s_part += int(s_part[i])

        return s_f_part == s_s_part
    else:
        return z


"""Завдання 1
Напишіть функцію, яка виводить на екран форматований текст, наведений нижче:

“Don’t let the noise of others’ opinions
drown out your own inner voice.”
                            Steve Jobs
"""

txt = "Don’t let the noise of others’ opinions drown out your own inner voice. Steve Jobs"
t_text = listText(txt)
print("Вивід форматованого тексту:\n")
print(t_text)
print('-' * 20, '\n')

"""Завдання 2 
Напишіть функцію, яка приймає два числа як параметр і відображає усі непарні числа між ними.
"""

x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
print()
viewOddNumbers(x, y)
print('-' * 20, '\n')

"""Завдання 3
Напишіть функцію, яка відображає горизонтальну або вертикальну лінію з певного символу. Функція приймає 
як параметр: довжину лінії, напрям та символ.
"""

dov_lin = int(input("Введіть довжину лінії: "))
napryam = int(input(f"Оберіть напрям (введіть число):\n1. Горизонтально\n2. Вертикально\n: "))
simv = input("Введіть символ заповнення лінії: ")
print()
printLine(dov_lin, napryam, simv)
print('-' * 20, '\n')

"""Завдання 4
Напишіть функцію, яка повертає максимальне число із чотирьох. Числа передаються як параметри.
"""

x1 = int(input("Введіть перше число: "))
x2 = int(input("Введіть друге число: "))
x3 = int(input("Введіть третє число: "))
x4 = int(input("Введіть четверте число: "))
print()
maxFromFour(x1, x2, x3, x4)
print('-' * 20, '\n')

"""Завдання 5
Напишіть функцію, яка повертає суму чисел у вказаному діапазоні. Межі діапазону передаються як параметри
"""

d_min = int(input("Введіть початок діапазону: "))
d_max = int(input("Введіть кінець діапазону: "))
print()
sumFromDiapason(d_min, d_max)
print('-' * 20, '\n')

"""
Завдання 6
Напишіть функцію, яка перевіряє чи є число простим. Число передається як параметр.
Якщо число просте, поверніть з методу true, якщо ні — false.
"""

x = int(input("Введіть число для перевірки: "))
print()
x_prov = provPrimeNumber(x)
print(f"{x_prov}")
print('-' * 20, '\n')

"""
Завдання 7
Напишіть функцію, яка перевіряє чи є шестизначне число «щасливим». Число передається як параметр.
Якщо число щасливе, поверніть з функції true, якщо ні — false.
«Щасливе шестизначне число» — це число, в якому сума перших трьох цифр дорівнює сумі других трьох цифр.
Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а 723422 — нещасливе 7+2+3 != 4+2+2.
"""
x = input("Введіть шестизначне число для перевірки: ")
print()
x_prov = provLuckNumber(x)
print(x_prov)
print('-' * 20)
