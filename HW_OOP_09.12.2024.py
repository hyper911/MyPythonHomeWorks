"""Рoзширте клас студента, додавши йому атрибут гроші,
реалізуйте можливість заробітку, під час відпочинку гроші витрачаються.
Глибше продумайте поведінку студента, наприклад, якщо бракує коштів -
він має піти на роботу, якщо проблеми з навчанням - то вчитися."""

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("I'm study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I'm sllep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Відрахували")
            self.alive = False
        elif self.gladness <= 0:
            print("Йому потрібний друг")
            self.alive = False
        elif self.progress > 5:
            print("Закінчив курс екстерном")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def live(self, day):
        print(f"Day {day} of {self.name}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

bohdan = Student("Bohdan")
for day in range(355):
    if bohdan.alive == False:
        break
    bohdan.live(day)