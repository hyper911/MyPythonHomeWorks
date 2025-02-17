from uuid import uuid4


class Animal:
    def __init__(self, name, weight, state_of_health):
        self.name = name
        self.weight = weight
        self.state_of_health = state_of_health
        self.id = str(uuid4())[0:8]

    def showInfo(self):
        print(f"Інформація про тварину:\n"
              f"Кличка: {self.name}\n"
              f"Вага: {self.weight}\n"
              f"ID: {self.id}\n"
              f"Стан: {self.state_of_health}")

    def treatTheAnimal(self):
        print('-' * 15)
        if self.state_of_health.lower().startswith("хвор"):
            print(f"На лікуванні: {self.name}")
            self.state_of_health = "Здоровий"
            print(f"Лікування {self.name} завершено!\n"
                  f"{self.name} {self.state_of_health.lower()}")
        elif self.state_of_health.lower().startswith("здор"):
            print(f"З {self.name} все добре! Лікування не потрібне!")
        else:
            print(f"Не вірний стан тварини!")
        print('-' * 15)


class TypeOfAnimal(Animal):
    def __init__(self, name, weight, state_of_health, type_pet):
        super().__init__(name, weight, state_of_health)
        self.type_pet = type_pet

    def showInfo(self):
        super().showInfo()
        print(f"Тип: {self.type_pet}")


Tuzik = TypeOfAnimal("Тузік", 12, "Хворий", "Собака")
Tuzik.showInfo()
Tuzik.treatTheAnimal()
Murzik = TypeOfAnimal("Мурзік", 6, "Здоровий", "Кіт")
Murzik.showInfo()
Murzik.treatTheAnimal()
