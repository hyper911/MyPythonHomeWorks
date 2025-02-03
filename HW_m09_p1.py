"""Завдання 1
Реалізуйте клас «Автомобіль». Збережіть у класі: назву
моделі, рік випуску, виробника, об’єм двигуна, колір машини,
ціну. Реалізуйте методи класу для введення-виведення даних
та інших операцій."""

class Car:
    def __init__(self, name, year, manufacturer, capacity, color, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.price = price

    def showInfo(self):
        print(f"Model: {self.name}\n"
              f"Year: {self.year}\n"
              f"Manufacturer: {self.manufacturer}\n"
              f"Capacity: {self.capacity}\n"
              f"Color: {self.color}\n"
              f"Price: {self.price}")

car = Car("Ford", 2020, "Ford", 6, "Red", 55000)

while True:
    user_choice = input(f"{'-' * 5}Car{'-' * 5}\n"
                        f"1. Show car\n"
                        f"2. Replace car\n"
                        f"3. Delete car\n"
                        f"4. Exit\n")
    if user_choice.startswith("1"):
        Car.showInfo(car)
    elif user_choice.startswith("2"):
        car_name = input(f"Enter car name: ")
        car_year = int(input(f"Enter car year: "))
        car_manufacturer = input(f"Enter car manufacturer: ")
        car_capacity = int(input(f"Enter car capacity: "))
        car_color = input(f"Enter car color: ")
        car_price = int(input(f"Enter car price: "))
        if car_name == "" or car_year == "" or car_manufacturer == "" or car_capacity == "" or car_color == "" or car_price == "":
            raise Exception("Value cannot be empty!")
        car = Car(car_name, car_year, car_manufacturer, car_capacity, car_color, car_price)
    elif user_choice.startswith("3"):
        del car
        print("Car is deleted!")
    elif user_choice.startswith("4"):
        print("Bye!")
        break
    else:
        print("Invalid input!")

"""
Завдання 2
Реалізуйте клас «Книга». Збережіть у класі: назву книги, 
рік видання, видавця, жанр, автора, ціну. Реалізуйте методи 
класу для введення-виведення даних та інших операцій."""

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def showInfo(self):
        print(f"Name: {self.name}\n"
              f"Year: {self.year}\n"
              f"Publisher: {self.publisher}\n"
              f"Genre: {self.genre}\n"
              f"Author: {self.author}\n"
              f"Price: {self.price}")

book = Book("It!", 2001, "NY print", "Horror", "Stephen King", 300)

while True:
    user_choice = input(f"{'-' * 5}Book{'-' * 5}\n"
                        f"1. Show book\n"
                        f"2. Replace book\n"
                        f"3. Delete book\n"
                        f"4. Exit\n")
    if user_choice.startswith("1"):
        Book.showInfo(book)
    elif user_choice.startswith("2"):
        book_name = input(f"Enter book name: ")
        book_year = int(input(f"Enter book year: "))
        book_publisher = input(f"Enter book publisher: ")
        book_genre = input(f"Enter book genre: ")
        book_author = input(f"Enter book author: ")
        book_price = int(input(f"Enter book price: "))
        if book_name == "" or book_year == "" or book_publisher == "" or book_genre == "" or book_author == "" or book_price == "":
            raise Exception("Value cannot be empty!")
        book = Book(book_name, book_year, book_publisher, book_genre, book_author, book_price)
    elif user_choice.startswith("3"):
        del book
        print("Book is deleted!")
    elif user_choice.startswith("4"):
        print("Bye!")
        break
    else:
        print("Invalid input!")

"""
Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
Реалізуйте методи класу для введення-виведення даних та інших операцій."""

class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def showInfo(self):
        print(f"Name: {self.name}\n"
              f"Year: {self.year}\n"
              f"Country: {self.country}\n"
              f"City: {self.city}\n"
              f"Capacity: {self.capacity}\n")

stadium = Stadium("Dynamo", 1995, "Ukraine", "Kyiv",  100000)

while True:
    user_choice = input(f"{'-' * 5}Stadium{'-' * 5}\n"
                        f"1. Show stadium\n"
                        f"2. Replace stadium\n"
                        f"3. Close stadium\n"
                        f"4. Exit\n")
    if user_choice.startswith("1"):
        Stadium.showInfo(stadium)
    elif user_choice.startswith("2"):
        stadium_name = input(f"Enter stadium name: ")
        stadium_year = int(input(f"Enter stadium open year: "))
        stadium_country = input(f"Enter stadium country: ")
        stadium_city = input(f"Enter stadium city: ")
        stadium_capacity = int(input(f"Enter stadium capacity: "))
        if stadium_name == "" or stadium_year == "" or stadium_country == "" or stadium_city == "" or stadium_capacity == "":
            raise Exception("Value cannot be empty!")
        stadium = Stadium(stadium_name, stadium_year, stadium_country, stadium_city, stadium_capacity)
    elif user_choice.startswith("3"):
        del stadium
        print("Stadium is closed!")
    elif user_choice.startswith("4"):
        print("Bye!")
        break
    else:
        print("Invalid input!")