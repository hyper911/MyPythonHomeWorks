import random

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Volvo": {"fuel": 75, "strength": 60, "consumption": 8},
    "ЗАЗ": {"fuel": 45, "strength": 30, "consumption": 15},
    "Ford": {"fuel": 80, "strength": 130, "consumption": 4}
}

job_list = {
    "Java dev": {"salary": 50, "gladness_less": 10},
    "Python dev": {"salary": 40, "gladness_less": 3},
    "Assembler dev": {"salary": 1000, "gladness_less": 25},
    "Swift dev": {"salary": 44, "gladness_less": 2}

}


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 20:
            self.shopping("food")
        if self.satiety >= 100:
            self.satiety = 100
        self.satiety += 20
        self.home.food -= 15
        print("I'm eating!")

    def work(self):
        if self.car.drive:
            self.car.drive()
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        print("I'm working....")
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive:
            self.car.drive()
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.car.fuel += 50
            self.money -= 50
            print("I bought fuel")
            if self.car.fuel > brands_of_car.get(self.car.brand)['fuel']:
                self.home.fuel += self.car.fuel - brands_of_car.get(self.car.brand)['fuel']
        elif manage == "food":
            self.money -= 50
            self.home.food += 30
            print("I bought foods")
        elif manage == "delicacies":
            self.gladness += 15
            self.satiety += 10
            self.money -= 25
            print("I bought and eat delicacies")
        self.satiety -= 5

    def fuel_with_home(self):
        if self.home.fuel >= self.car.consumption:
            self.home.fuel -= self.car.consumption
            self.car.fuel += self.car.consumption
            print("I use fuel from home")
        else:
            self.shopping("fuel")

    def chill(self):
        print("I'm chilling...")
        self.gladness += 20
        self.home.mess += 2
        self.satiety -= 5

    def clean_home(self):
        print("I'm cleaning home...")
        self.gladness -= 5
        self.home.mess = 0
        self.satiety -= 5

    def to_repair(self):
        print("I'm repairing car...")
        if self.car.drive:
            self.car.drive()
        self.car.strength += 100
        self.money -= 100
        self.satiety -= 5
        if self.car.strength > brands_of_car.get(self.car.brand)['strength']:
            self.car.strength = brands_of_car.get(self.car.brand)['strength']


    def day_index(self, day):
        print(f"Today the {day} of {self.name}\n"
              f"{'-' * 25}")
        print(f"Money: {self.money} $\nSatiety: {self.satiety}\tGladness: {self.gladness}")
        print(f"Food: {self.home.food}\tMess: {self.home.mess}")
        print(f"Fuel: {self.car.fuel} + {self.home.fuel}\tStrength: {self.car.strength}\n"
              f"{'-' * 25}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead..")
            return False
        if self.money < -500:
            print("Bankrot")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
            print("set Home")
        if self.car is None:
            self.get_car()
            print(f"set Car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I got job {self.job.job} with salary {self.job.salary}")
        # Доробіть симуліцію життя персонажа в цьому методі напишіть код нижче
        print('*' * 30)
        self.day_index(day)
        self.home.mess += 1
        if self.money <= 200:
            self.work()
        if self.satiety <= 15:
            self.eat()
        if self.gladness <= 15:
            self.chill()
        if self.shopping("food") and self.satiety <= 10:
            self.shopping("delicacies")
        if self.home.mess > 2:
            self.clean_home()
        if self.car.fuel <= self.car.consumption:
            self.fuel_with_home()
        if self.car.strength <= 5:
            self.to_repair()
        print('*' * 30)


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brands_of_car[self.brand]["fuel"]
        self.strength = brands_of_car[self.brand]["strength"]
        self.consumption = brands_of_car[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cant move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.fuel = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Alex")

for day in range(1, 365):
    if nick.live(day) == False:
        break
