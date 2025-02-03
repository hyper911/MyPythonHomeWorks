def printInfo(myList):
    print()
    print("---Країни---")
    for ind, item in enumerate(myList):
        print(ind + 1, item)
    print('-' * 12, '\n')


"""
Завдання 1
Маємо множину з назвами країн. Надайте користувачеві можливість:
■ додавати країни;
■ видаляти країни;
■ пошуку країн за введеними символами;
■ перевіряти, чи міститься країна в множині.
"""

countrySet = {"Україна", "США", "Канада", "Угорщина", "Бразилія", "Германія"}
print(f"Міні гра \n{'-' * 10}")
while True:
    userchoice = input(
        f"-Меню-\n1. Додати країну \n2. Видалити країну \n3. Пошук країни \n4. Перевірити, чи є країна у списку \n5. Вихід \nВведіть цифру меню: ")
    if userchoice.startswith("1"):
        user_add_country = input(f"Введіть назву країни: ").lower().strip()
        user_add_country = user_add_country.capitalize()
        if user_add_country == "":
            print("Назва не може бути пустою!")
            pass
        else:
            countrySet.add(user_add_country)
    elif userchoice.startswith("2"):
        user_del_country = input(f"Введіть назву країни: ").lower().strip()
        user_del_country = user_del_country.capitalize()
        if user_del_country == "":
            print("Назва не може бути пустою!")
            pass
        else:
            countrySet.remove(user_del_country)
    elif userchoice.startswith("3"):
        user_f_country = input(f"Введіть літери для пошуку країни: ").lower().strip()
        if user_f_country == "":
            print("Пошук не заповнений!")
            pass
        else:
            list_of_find = []
            for country in countrySet:
                if user_f_country.lower().strip() in country.lower():
                    list_of_find.append(country)

            if len(list_of_find) > 0:
                print()
                print(f"Знайдені країни:")
                for country in list_of_find:
                    print(country)
            else:
                print("Країни за Вашим запитом не знайдені!")
    elif userchoice.startswith("4"):
        user_find_country = input(f"Введіть назву країни для пошуку: ").lower().strip()
        user_find_country = user_find_country.capitalize()
        if user_find_country == "":
            print("Назва країни не може бути пустою!")
            pass
        else:
            if user_find_country in countrySet:
                print("Країна є у списку")
            else:
                print("Країни немає у списку!")
    elif userchoice.startswith("5"):
        print("Дякуємо за увагу! До нових зустрічей!")
        break
    else:
        print("Не вірний номер меню!")
        pass

    printInfo(countrySet)
print('-' * 15, '\n')

"""Завдання 2
Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які є в обох множинах.
"""

townSet1 = {"Київ", "Харків", "Біла Церква", "Торонто", "Львів", "Дубай"}
townSet2 = {"Київ", "Івано-Франківськ", "Бориспіль", "Львів", "Харків", "Чернигів"}
townSet3 = townSet2.intersection(townSet1)
print(f"Множина з спільними містами: \n{townSet3}")
print('-' * 15, '\n')

"""Завдання 3
Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які містяться в першій множині, але відсутні у другій.
"""

townSet1 = {"Київ", "Харків", "Біла Церква", "Торонто", "Львів", "Дубай"}
townSet2 = {"Київ", "Івано-Франківськ", "Бориспіль", "Львів", "Харків", "Чернигів"}
townSet3 = townSet1.difference(townSet2)
print(f"Множина: \n{townSet3}")
print('-' * 15, '\n')

"""Завдання 4
Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які містяться в другій множині, але відсутні в першій.
"""

townSet1 = {"Київ", "Харків", "Біла Церква", "Торонто", "Львів", "Дубай"}
townSet2 = {"Київ", "Івано-Франківськ", "Бориспіль", "Львів", "Харків", "Чернигів"}
townSet3 = townSet2.difference(townSet1)
print(f"Множина: \n{townSet3}")
print('-' * 15, '\n')

"""Завдання 5
Маємо дві множини з назвами міст. Створіть третю множину з унікальними назвами для кожної множини.
"""

townSet1 = {"Київ", "Харків", "Біла Церква", "Торонто", "Львів", "Дубай"}
townSet2 = {"Київ", "Івано-Франківськ", "Бориспіль", "Львів", "Харків", "Чернигів"}
townSet3 = townSet2.union(townSet1)
print(f"Множина: \n{townSet3}")
print('-' * 15, '\n')

"""Завдання 6
У словнику зберігається набір пар: Назва країни -> Столиця.
Реалізуйте функціональність за додаванням, видаленням, пошуком, заміною.
"""

myCountrySet = {}
while True:
    userchoice = input(
        f"-Меню-\n1. Додати країну \n2. Видалити країну \n3. Пошук країни \n4. Заміна країни \n5. Вихід \nВведіть "
        f"цифру "
        f"меню: ")
    if userchoice.startswith("1"):
        user_add_country = input(f"Введіть назву країни: ").lower().strip()
        user_add_country_capital = input(f"Введіть назву столиці: ").lower().strip()
        user_add_country = user_add_country.capitalize()
        user_add_country_capital = user_add_country_capital.capitalize()
        if user_add_country == "" or user_add_country_capital == "":
            print("Назва не може бути пустою!")
            pass
        else:
            myCountrySet = {"name": user_add_country, "capital": user_add_country_capital}

    elif userchoice.startswith("2"):
        user_del_country = input(f"Введіть назву країни: ").lower().strip()
        user_del_country = user_del_country.capitalize()
        if user_del_country == "":
            print("Назва не може бути пустою!")
            pass
        else:
            if user_del_country == myCountrySet["name"]:
                myCountrySet.clear()
                print("Країна та ії столиця видалені!")
            else:
                print("Країна не знайдена!")
                pass
    elif userchoice.startswith("3"):
        user_find_country = input(f"Введіть назву країни для пошуку: ").lower().strip()
        user_find_country = user_find_country.capitalize()
        if user_find_country == "":
            print("Назва країни не може бути пустою!")
            pass
        else:
            if user_find_country == myCountrySet["name"]:
                print("Країна є у списку")
            else:
                print("Країни немає у списку!")
    elif userchoice.startswith("4"):
        user_find_country = input(f"Введіть назву країни, яку хочете замінити : ").lower().strip()
        user_find_country_replace = input(f"Введіть назву країни: ").lower().strip()
        user_find_country_capital_replace = input(f"Введіть назву столиці: ").lower().strip()
        user_find_country = user_find_country.capitalize()
        user_find_country_replace = user_find_country_replace.capitalize()
        user_find_country_capital_replace = user_find_country_capital_replace.capitalize()
        if user_find_country_replace == "" or user_find_country_capital_replace == "":
            print("Назва не може бути пустою!")
            pass
        else:
            if user_find_country == myCountrySet["name"]:
                myCountrySet = {"name": user_find_country_replace,
                                "capital": user_find_country_capital_replace}
                print("Країна та столиця змінені!")
            else:
                print("Країна не знайдена!")
                pass
    elif userchoice.startswith("5"):
        print("Дякуємо за увагу! Гарного дня!")
        break
    else:
        print("Не вірний номер меню!")
        pass

    print()
    for name, capital in myCountrySet.items():
        print(f"{name}: {capital}")
    print()