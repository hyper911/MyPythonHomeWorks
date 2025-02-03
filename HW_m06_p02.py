"""Завдання 1
Створіть програму, що містить інформацію про відомих баскетболістів.
Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
Використовуйте словник для збереження інформації.
"""

myDict = {}.fromkeys(["LeBron James", "Shaquille O'Neal", "Michael Jordan"], 0)
myDict["Michael Jordan"] = 198
myDict["LeBron James"] = 206
myDict["Shaquille O'Neal"] = 216
print(f"\n---Відомі баскетболісти---")

while True:
    user_choice = input(f"{str("-=Меню=-").rjust(16)}\n"
                        f"1. Додати баскетболіста.\n"
                        f"2. Видалити баскетболіста.\n"
                        f"3. Знайти баскетболіста.\n"
                        f"4. Змінити дані баскетболіста.\n"
                        f"5. Вихід.\n"
                        f"Оберіть цифру меню: ")
    if user_choice.startswith("1"):
        user_add_basket_player = input(f"Введіть ПІБ баскетболіста: ").lower().strip().title()
        user_add_basket_player_height = int(input(f"Введіть висоту баскетболіста: "))
        if (user_add_basket_player not in myDict.keys() and user_add_basket_player != "" and
                user_add_basket_player_height > 0):
            myDict.update({user_add_basket_player: user_add_basket_player_height})
        else:
            print(f"Такий гравець вже існує в словнику!")
            pass
    if user_choice.startswith("2"):
        user_del_basker_player = input(f"Введіть ПІБ баскетболіста: ").lower().strip().title()
        if user_del_basker_player in myDict.keys():
            myDict.pop(user_del_basker_player)
            print(f"Баскетболіст {user_del_basker_player} видалений!")
        else:
            print(f"Такого гравця немає в словнику!")
            pass
    if user_choice.startswith("3"):
        user_find_basket_player = input(f"Введіть слово для пошуку: ").lower().strip()
        print(f"Знайдені баскетболісти: ")
        for i in myDict.keys():
            if user_find_basket_player in i.lower():
                print(i)
            else:
                pass
    if user_choice.startswith("4"):
        user_change_basket_player = input(f"Введіть ПІБ баскетболіста: ").lower().strip().title()
        user_change_basket_player_new = input(f"Якщо потрібно редагувати ПІБ гравця введіть нові дані,\n"
                                              f"якщо ні - залиште пустим!: ").lower().strip().title()
        user_change_basket_player_height = int(input(f"Введіть висоту баскетболіста: "))
        if user_change_basket_player in myDict.keys():
            if user_change_basket_player_new == "":
                myDict.update({user_change_basket_player: user_change_basket_player_height})
            else:
                if user_change_basket_player_new not in myDict.keys() and user_change_basket_player_height > 0:
                    myDict.pop(user_change_basket_player)
                    myDict.update({user_change_basket_player_new: user_change_basket_player_height})
                else:
                    print(f"Такий гравець вже існує в словнику!")
                    pass
        else:
            print(f"Такого гравця немає в словнику!")
            pass
    if user_choice.startswith("5"):
        print(f"\nДо побачення!")
        print('-' * 15)
        break

    print(f"\nСловник з баскетболістами:")
    for item in myDict.items():
        print(item)

    print()

"""Завдання 2
Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку. 
Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник для збереження інформації.
"""

myEngDict = {}.fromkeys(["Day", "Weather", "Week"], "")
myEngDict["Day"] = "Jour"
myEngDict["Weather"] = "Météo"
myEngDict["Week"] = "Semaine"
print(f"\n---Англо-французький словник---")

while True:
    user_choice = input(f"{str("-=Меню=-").rjust(16)}\n"
                        f"1. Додати слово.\n"
                        f"2. Видалити слово.\n"
                        f"3. Знайти слово.\n"
                        f"4. Змінити переклад.\n"
                        f"5. Вихід.\n"
                        f"Оберіть цифру меню: ")
    if user_choice.startswith("1"):
        user_add_eng_word = input(f"Введіть слово англійською: ").lower().strip().title()
        user_add_fr_translation = input(f"Введіть переклад слова французькою: ").lower().strip().title()
        if (user_add_eng_word not in myEngDict.keys() and user_add_eng_word != "" and user_add_fr_translation != ""):
            myEngDict.update({user_add_eng_word: user_add_fr_translation})
        else:
            print(f"Таке слово вже є в словнику!")
            pass
    if user_choice.startswith("2"):
        user_del_eng_word = input(f"Введіть слово англійською: ").lower().strip().title()
        if user_del_eng_word in myEngDict.keys():
            myEngDict.pop(user_del_eng_word)
            print(f"Слово {user_del_eng_word} видалено!")
        else:
            print(f"Такого слова немає в словнику!")
            pass
    if user_choice.startswith("3"):
        user_find_eng_word = input(f"Введіть частину слова англійською для пошуку: ").lower().strip()
        print(f"Знайдені слова: ")
        for i in myEngDict.keys():
            if user_find_eng_word in i.lower():
                print(i)
            else:
                pass
    if user_choice.startswith("4"):
        user_change_eng_word = input(f"Введіть слово англійською: ").lower().strip().title()
        user_change_eng_word_new = input(f"Якщо потрібно редагувати слово введіть нові дані,\n"
                                         f"якщо ні - залиште пустим!: ").lower().strip().title()
        user_change_fr_translation = input(f"Введіть переклад слова французькою: ").lower().strip().title()
        if user_change_eng_word in myEngDict.keys():
            if user_change_eng_word_new == "":
                myEngDict.update({user_change_eng_word: user_change_fr_translation})
            else:
                if user_change_eng_word_new not in myEngDict.keys() and user_change_fr_translation != "":
                    myEngDict.pop(user_change_eng_word)
                    myEngDict.update({user_change_eng_word_new: user_change_fr_translation})
                else:
                    print(f"Таке слово вже є в словнику!")
                    pass
        else:
            print(f"Такого слова немає в словнику!")
            pass
    if user_choice.startswith("5"):
        print(f"\nДо побачення!")
        print('-' * 15)
        break

    print(f"\nАнгло-французьский словник:")
    for item in myEngDict.items():
        print(item)
    print()

"""Завдання 3
Створіть програму «Фірма», яка зберігає інформацію про працівників:
ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype.
Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник для збереження інформації.
"""

myCorpDict = {}.fromkeys(["Пупкін Василь Петрович", "Звичайний Опанас Миколайович", "Сплячий Дмитро Володимирович"], [])
myCorpDict["Пупкін Василь Петрович"] = ["+380960980887", "vpupkin@corp.com", "Директор", "501", "vpupkin"]
myCorpDict["Звичайний Опанас Миколайович"] = ["+380931568911", "zvich@corp.com", "Головний бухгалтер", "515", "zvich"]
myCorpDict["Сплячий Дмитро Володимирович"] = ["+380678975569", "splyach@corp.com", "Менеджер", "516", "splyach"]
print(f"\n---Фірма---")

while True:
    user_choice = input(f"{str("-=Меню=-").rjust(16)}\n"
                        f"1. Додати працівника.\n"
                        f"2. Видалити працівника.\n"
                        f"3. Знайти працівника.\n"
                        f"4. Змінити дані працівника.\n"
                        f"5. Вихід.\n"
                        f"Оберіть цифру меню: ")
    if user_choice.startswith("1"):
        user_add_corp_worker = input(f"Введіть ПІБ працівника: ").lower().strip().title()
        user_add_corp_worker_tel = input(f"Введіть телефон працівника: ")
        user_add_corp_worker_email = input(f"Введіть email працівника: ")
        user_add_corp_worker_job_title = input(f"Введіть посаду працівника: ")
        user_add_corp_worker_cab_number = input(f"Введіть номер кабінету працівника: ")
        user_add_corp_worker_skype = input(f"Введіть скайп працівника: ")
        list_of_params = [user_add_corp_worker_tel, user_add_corp_worker_email,
                          user_add_corp_worker_job_title, user_add_corp_worker_cab_number, user_add_corp_worker_skype]

        if (user_add_corp_worker not in myCorpDict.keys() and user_add_corp_worker != "" and user_add_corp_worker_tel
                != "" and user_add_corp_worker_email != "" and user_add_corp_worker_job_title != ""):
            myCorpDict.update({user_add_corp_worker: list_of_params})
        else:
            print(f"Такий працівник вже існує в словнику!")
            pass
    if user_choice.startswith("2"):
        user_del_corp_worker = input(f"Введіть ПІБ працівника: ").lower().strip().title()
        if user_del_corp_worker in myCorpDict.keys():
            myCorpDict.pop(user_del_corp_worker)
            print(f"Працівник {user_del_corp_worker} видалений!")
        else:
            print(f"Такого працівника немає в словнику!")
            pass
    if user_choice.startswith("3"):
        user_find_corp_worker = input(f"Введіть частину ПІБ для пошуку працівника: ").lower().strip()
        print(f"Знайдені працівники: ")
        for i in myCorpDict.keys():
            if user_find_corp_worker in i.lower():
                print(i)
            else:
                pass
    if user_choice.startswith("4"):
        user_change_corp_worker = input(f"Введіть ПІБ працівника: ").lower().strip().title()
        user_change_corp_worker_new = input(f"Якщо потрібно редагувати ПІБ працівника введіть нові дані,\n"
                                            f"якщо ні - залиште пустим!: ").lower().strip().title()
        user_change_corp_worker_tel = input(f"Введіть телефон працівника: ")
        user_change_corp_worker_email = input(f"Введіть email працівника: ")
        user_change_corp_worker_job_title = input(f"Введіть посаду працівника: ")
        user_change_corp_worker_cab_number = input(f"Введіть номер кабінету працівника: ")
        user_change_corp_worker_skype = input(f"Введіть скайп працівника: ")
        list_of_params_change = [user_change_corp_worker_tel, user_change_corp_worker_email,
                                 user_change_corp_worker_job_title, user_change_corp_worker_cab_number,
                                 user_change_corp_worker_skype]
        if user_change_corp_worker in myCorpDict.keys():
            if user_change_corp_worker_new == "":
                myCorpDict.update({user_change_corp_worker: list_of_params_change})
            else:
                if (user_change_corp_worker_new not in myCorpDict.keys() and user_change_corp_worker_tel != "" and
                        user_change_corp_worker_email != "" and user_change_corp_worker_job_title != ""):
                    myCorpDict.pop(user_change_corp_worker)
                    myCorpDict.update({user_change_corp_worker_new: list_of_params_change})
                else:
                    print(f"Такий працівник вже існує в словнику!")
                    pass
        else:
            print(f"Такого працівника немає в словнику!")
            pass
    if user_choice.startswith("5"):
        print(f"\nДо побачення!")
        print('-' * 15)
        break

    print(f"\nПрацівники фірми:")
    for item in myCorpDict.items():
        print(item)
    print()

"""Завдання 4
Створіть програму «Книжкова колекція», яка зберігає інформацію про книги:
автор, назва книги, жанр, рік випуску, кількість сторінок, видавництво.
Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник для збереження інформації.
"""

myBookDict = {}.fromkeys(["Коммісар Мегре", "Воно"], [])
myBookDict["Коммісар Мегре"] = ["Сімеон Жорж", "Детектив", "1993 р.", "448 с.", "Київ Україна"]
myBookDict["Воно"] = ["Кінг Стівен", "Фентезі", "1990 р.", "1344 с.", "КСД"]
print(f"\n---Книжкова колекція---")

while True:
    user_choice = input(f"{str("-=Меню=-").rjust(16)}\n"
                        f"1. Додати книгу.\n"
                        f"2. Видалити книгу.\n"
                        f"3. Знайти книгу.\n"
                        f"4. Змінити дані книги.\n"
                        f"5. Вихід.\n"
                        f"Оберіть цифру меню: ")
    if user_choice.startswith("1"):
        user_add_book = input(f"Введіть назву книги: ").lower().strip().capitalize()
        user_add_book_autor = input(f"Введіть ПІБ автора: ").lower().strip().title()
        user_add_book_genre = input(f"Введіть жанр книги: ")
        user_add_book_year = input(f"Введіть рік випуску: ") + " р."
        user_add_book_count_pages = input(f"Введіть кількість сторінок: ") + " с."
        user_add_book_manufacturer = input(f"Введіть назву видавництва: ")
        list_of_params = [user_add_book_autor, user_add_book_genre, user_add_book_year, user_add_book_count_pages,
                          user_add_book_manufacturer]

        if (user_add_book not in myBookDict.keys() and user_add_book != "" and user_add_book_autor
                != "" and user_add_book_genre != "" and user_add_book_year != "" and user_add_book_count_pages != "" and user_add_book_manufacturer != ""):
            myBookDict.update({user_add_book: list_of_params})
        else:
            print(f"Така книга вже існує в колекції!")
            pass
    if user_choice.startswith("2"):
        user_del_book = input(f"Введіть назву книги: ").lower().strip().capitalize()
        if user_del_book in myBookDict.keys():
            myBookDict.pop(user_del_book)
            print(f"Книга {user_del_book} видалена!")
        else:
            print(f"Такої книги немає в колекціїі!")
            pass
    if user_choice.startswith("3"):
        user_find_book = input(f"Введіть частину назви книги для пошуку: ").lower().strip()
        print(f"Знайдені книги: ")
        for i in myBookDict.keys():
            if user_find_book in i.lower():
                print(i)
            else:
                pass
    if user_choice.startswith("4"):
        user_change_book = input(f"Введіть назву книги: ").lower().strip().capitalize()
        user_change_book_new = input(f"Якщо потрібно редагувати назву книги - введіть нові дані,\n"
                                     f"якщо ні - залиште пустим!: ").lower().strip().capitalize()
        user_change_book_autor = input(f"Введіть ПІБ автора: ").lower().strip().title()
        user_change_book_genre = input(f"Введіть жанр книги: ")
        user_change_book_year = input(f"Введіть рік випуску: ") + " р."
        user_change_book_count_pages = input(f"Введіть кількість сторінок: ") + " с."
        user_change_book_manufacturer = input(f"Введіть назву видавництва: ")
        list_of_params_change = [user_change_book_autor, user_change_book_genre, user_change_book_year,
                                 user_change_book_count_pages, user_change_book_manufacturer]
        if user_change_book in myBookDict.keys():
            if user_change_book_new == "":
                myBookDict.update({user_change_book: list_of_params_change})
            else:
                if (user_change_book_new not in myBookDict.keys() and user_change_book_autor != "" and
                        user_change_book_genre != "" and user_change_book_year != "" and user_change_book_count_pages
                        != "" and user_change_book_manufacturer != ""):
                    myBookDict.pop(user_change_book)
                    myBookDict.update({user_change_book_new: list_of_params_change})
                else:
                    print(f"Така книга вже існує в колекції!")
                    pass
        else:
            print(f"Такої книги немає в колекції!")
            pass
    if user_choice.startswith("5"):
        print(f"\nДо побачення!")
        print('-' * 15)
        break

    print(f"\nКниги в колекції:")
    for item in myBookDict.items():
        print(item)
    print()
