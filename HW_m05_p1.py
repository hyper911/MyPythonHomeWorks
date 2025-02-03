from random import randint


def sortMyList(myList):
    mArif = sum(myList) / len(myList)
    tmp_list = []
    if mArif > 0:
        print(f"\n"
              f"Дві третини списку сортуємо за зростанням:")
        l = (len(myList) // 3) * 2
        left_part = myList[:l]
        right_part = myList[l:]
        left_part.sort()
        right_part.reverse()
        for i in range(len(left_part)):
            tmp_list.append(left_part[i])
        for i in range(len(right_part)):
            tmp_list.append(right_part[i])
        for i in range(len(myList)):
            myList[i] = tmp_list[i]
    else:
        print(f"\n"
              f"Першу третину списку сортуємо за зростанням:")
        l = len(myList) // 3
        left_part = myList[:l]
        right_part = myList[l:]
        left_part.sort()
        right_part.reverse()
        for i in range(len(left_part)):
            tmp_list.append(left_part[i])
        for i in range(len(right_part)):
            tmp_list.append(right_part[i])
        for i in range(len(myList)):
            myList[i] = tmp_list[i]


def printInfo(myList):
    print()
    print("-Оцінки-")
    for ind, item in enumerate(myList):
        print(ind + 1, '\t', item)
    print('-' * 12, '\n')


def programUspishnist():
    listOfRating = []
    print(f"\n"
          f"-= Програма \"Успішність\" =- \n"
          f"{'-' * 21}")

    for i in range(10):
        x = 0
        while x not in range(1, 13):
            x = int(input(f"Введіть оцінку (від 1 до 12) № {i + 1}: "))
        else:
            listOfRating.append(x)
    print()

    while True:
        user_choice = input(f"-=Меню=-\n"
                            f"1. Виведення оцінок.\n"
                            f"2. Перескладання іспиту.\n"
                            f"3. Отримання стипендії. \n"
                            f"4. Виведення оцінок з сортуванням.\n"
                            f"5. Вихід.\n"
                            f"Введіть цифру меню: ")
        if user_choice.startswith("1"):
            printInfo(listOfRating)
        elif user_choice.startswith("2"):
            u_choice_index_of_element = 0
            u_choice_new_rating = 0
            while u_choice_index_of_element not in range(1, len(listOfRating)):
                u_choice_index_of_element = int(input("Введіть номер елементу списку (від 1 до 10): "))
            while u_choice_new_rating not in range(1, 13):
                u_choice_new_rating = int(input("Введіть нову оцінку (від 1 до 12): "))
            else:
                listOfRating[u_choice_index_of_element - 1] = u_choice_new_rating
                print(f"\n"
                      f"Оцінка номер {u_choice_index_of_element} змінена на {u_choice_new_rating}. Вітаємо!\n")
                pass
        elif user_choice.startswith("3"):
            m_rating = round(sum(listOfRating) / len(listOfRating))
            if m_rating >= 10.7:
                print(f"\n"
                      f"Стипендія дозволена!\n")
            else:
                print(f"\n"
                      f"Середній бал нижче 10.7! Стипендія не дозволена!\n")
        elif user_choice.startswith("4"):
            s_list = list(listOfRating)
            u_choice_sort_direction = input(f"\n"
                                            f"Оберіть направлення сортування:\n"
                                            f"1. Зростання.\n"
                                            f"2. Спадання.\n"
                                            f"Введіть цифру з меню: ")
            if u_choice_sort_direction.startswith("1"):
                s_list.sort()
                print(f"Cписок оцінок (за зростанням): \n")
                printInfo(s_list)
            else:
                s_list.sort(reverse=True)
                print(f"Cписок оцінок (за спаданням): \n")
                printInfo(s_list)
        elif user_choice.startswith("5"):
            print(f"\n"
                  f"Дякуємо за увагу! Гарного дня!\n")
            break
        else:
            print(f"\n"
                  f"Не вірно введений номер меню!\n")
            pass


def myBubleSortOptimize(myList):
    l = len(myList)
    for i in range(l - 1):
        c = 0
        for j in range(l - 1):
            if myList[j] > myList[j + 1]:
                tmp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = tmp
                c = 1
        if c == 0:
            print(f"\n"
                  f"Список відсортовано!")
            break
    return myList


"""Завдання 1
Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
якщо ні — тільки першу третину. Решту списку не сортуйте, а розташуйте у зворотному порядку
"""

myList = [randint(-50, 50) for _ in range(20)]
sortMyList(myList)
print(myList)

"""Завдання 2
Написати програму «Успішність».
Користувач вводить 10 оцінок студента. Оцінки від 1 до 12.
Реалізуйте меню для користувача:
■ виведення оцінок (виведення вмісту списку);
■ перескладання іспиту (користувач вводить номер елемента списку та нову оцінку);
■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
■ виведення відсортованого списку оцінок: за зростанням або спаданням.
"""

programUspishnist()

"""Завдання 3
Напишіть програму для сортування списку методом удосконаленого бульбашкового сортування.
Удосконалення полягає в тому, щоб аналізувати кількість перестановок на кожному кроці.
Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.
"""

myList = [randint(-50, 50) for _ in range(20)]
myBubleSortOptimize(myList)
print(myList)
