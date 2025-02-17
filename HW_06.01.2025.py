"""Задача 1: Створення клієнтських рахунків
Створіть клас BankAccount, який дозволяє створювати банківські рахунки з різними
початковими параметрами.
Перезавантажте метод ініціалізації __init__, щоб:
1. Якщо передано тільки name — створюється рахунок з початковим балансом 0.
2. Якщо передано name і initial_balance, задається початковий баланс.
3. Якщо передано name, initial_balance, і currency, встановлюється валюта
рахунку.
Приклад завдання:
• Створіть три об'єкти: один із балансом за замовчуванням, один із початковим
балансом, один із валютою "USD".
• Виведіть інформацію про кожен рахунок (ім'я, баланс, валюта)."""


class BankAccount:
    def __init__(self, name, initial_balance=0, currency="UAH"):
        self.name = name
        self.balance = initial_balance
        self.currency = currency
        self.transactions = []

    def __str__(self):
        return f"{self.name}, {self.balance} {self.currency}\n"

    def transactionHistory(self):
        print(f"{self.name} transaction history:\n"
              f"{self.transactions}")

    def deposit(self, money, coment=""):
        if isinstance(money, (int, float)) and coment == "":
            if money > 0:
                money = abs(money)
                self.balance += money
        elif type(money) == list:
            for r in money:
                if r > 0:
                    r = abs(r)
                    self.balance += r
        elif isinstance(money, (int, float)) and coment != "":
            if money > 0:
                self.balance += money
                self.transactions.append({money: coment})

    def withdraw(self, money, currency="", cource=1):
        if isinstance(money, (int, float)) and currency == "":
            money = abs(money)
            if money > 0 and money <= self.balance:
                self.balance -= money
            else:
                print(f"Withdraw error! Not enough money!")
        elif isinstance(money, (int, float)) and currency != "" and cource != 1:
            money = abs(money)
            money *= cource
            if money > 0 and money <= self.balance:
                self.balance -= money
            else:
                print(f"Withdraw error! Not enough money!")
        elif isinstance(money, list):
            for r in money:
                if r > 0 and r <= self.balance:
                    r = abs(r)
                    self.balance -= r
                else:
                    print(f"Withdraw error! Not enough money!")

    def transfer(self, money, recipient=None, coment=""):
        if isinstance(money, (int, float)) and recipient == None and coment == "":
            if money > 0:
                recipient = User1
                recipient.balance += money
                self.balance -= money
        elif isinstance(money, (int, float)) and recipient != None and coment == "":
            if money > 0:
                money = abs(money)
                recipient.balance += money
                self.balance -= money
        elif isinstance(money, (int, float)) and recipient != None and coment != "":
            if money > 0:
                money = abs(money)
                recipient.balance += money
                self.balance -= money
                self.transactions.append({money: coment})

    def get_account_info(self, detailed=False, as_dict=False):
        if not detailed and not as_dict:
            print(f"{self.name}, {self.balance}")
        if detailed:
            print(f"{self.name}, {self.balance} {self.currency}\n"
                  f"Transactions: \n"
                  f"{self.transactions}\n"
                  f"Count transactions: {len(self.transactions)}")
        if as_dict:
            print(f"{self.__dict__}")


class PremiumAccount(BankAccount):
    def __init__(self, name, premium, initial_balance=0, currency="UAH"):
        super().__init__(name, initial_balance, currency)
        self.premium = True

    def deposit(self, money, coment=""):
        money = abs(money)
        money *= 1.01
        super().deposit(money, coment)

    def withdraw(self, money, coment=""):
        if isinstance(money, (int, float)) and self.premium:
            money = abs(money)
            if money > 0 and (self.balance - money) >= -1000:
                self.balance -= money
            else:
                print(f"Withdraw error! Not enough money!")

    def transfer(self, money, recipient=None, coment=""):
        if isinstance(money, (int, float)) and self.premium:
            money = abs(money)
            commission = money * 0.005
            if money > 0 and money <= self.balance:
                self.balance -= (money + commission)
                recipient.balance += money


# 1
print("*** Task 1 ***")
User1 = BankAccount("Alex")
User2 = BankAccount("John", 3300)
User3 = BankAccount("Jack", 350, currency="USD")
print(User1, User2, User3)

"""Задача 2: Операції з рахунком
Додайте до класу BankAccount метод deposit, який дозволяє поповнювати рахунок.
Перезавантажте метод deposit, щоб:
1. Якщо передано одну суму — поповнюється баланс на цю суму.
2. Якщо передано список сум — кожна сума додається до балансу.
3. Якщо передано суму і коментар (рядок), сума додається з відповідним записом 
у історії транзакцій.
Приклад завдання:
• Поповніть рахунок на 100.
• Поповніть рахунок на суми [50, 200, 300].
• Поповніть рахунок на 500 із коментарем "Зарплата".
• Виведіть поточний баланс і історію транзакцій."""

money_list = [50, 200, 300]

# 2
print("*** Task 2 ***")
User1.deposit(100)
User2.deposit(money_list)
User3.deposit(500, "Зарплата")
print(User1, User2, User3)
User3.transactionHistory()
print("")

"""Задача 3: Зняття грошей з рахунку
Додайте до класу BankAccount метод withdraw, який дозволяє знімати гроші.
Перезавантажте метод withdraw, щоб:
1. Якщо передано тільки суму — знімається ця сума.
2. Якщо передано суму та валюту, знімається сума в зазначеній валюті (за 
фіксованим курсом обміну).
3. Якщо передано список сум, суми знімаються по черзі.
Приклад завдання:
• Зніміть 100.
• Зніміть 50 у валюті "USD" (курс 1 USD = 40 UAH).
• Зніміть [20, 30, 50] за одну операцію.
• Виведіть поточний баланс."""

money_list = [20, 30, 50]

# 3
print("*** Task 3 ***")
User2.withdraw(100)
User2.withdraw(50, "USD", 40)
User2.withdraw(sum(money_list))
print(User2)

"""Задача 4: Переведення коштів між рахунками
Створіть метод transfer, який дозволяє переказувати гроші між рахунками.
Перезавантажте метод transfer, щоб:
1. Якщо передано лише суму — переказ відбувається на рахунок за 
замовчуванням.
2. Якщо передано суму і рахунок — переказ відбувається на зазначений рахунок.
3. Якщо передано суму, рахунок і коментар — переказ відбувається із записом 
коментаря.
Приклад завдання:
• Створіть два рахунки.
• Переказуйте гроші між ними різними способами.
• Виведіть залишок на кожному рахунку та історію транзакцій."""

# 4
print("*** Task 4 ***")
User4 = BankAccount("Tomas", 3000)
User5 = BankAccount("Bob", 600)
User4.transfer(600)
User4.transfer(300, User5)
User4.transfer(150, User5, "Transfer")
print(User4, User5)
User4.transactionHistory()
print("")

"""Задача 5: Інформація про рахунок
Додайте до класу BankAccount метод get_account_info, який виводить інформацію 
про рахунок.
Перезавантажте метод get_account_info, щоб:
1. Якщо викликається без параметрів — виводить ім'я власника та баланс.
2. Якщо передано параметр detailed=True, додає до інформації валюту, історію 
транзакцій та кількість транзакцій.
3. Якщо передано параметр as_dict=True, повертає інформацію у вигляді 
словника.
Приклад завдання:
• Викличте метод трьома різними способами.
• Виведіть результати у вигляді тексту та у вигляді словника."""

# 5
print("*** Task 5 ***")
User1.get_account_info()
User4.get_account_info(detailed=True)
User3.get_account_info(as_dict=True)
print("")

"""Задача 6: Багаторівневий банкінг
Додайте клас PremiumAccount, який успадковує BankAccount.
Перезавантажте методи, щоб:
1. Для поповнення рахунку deposit додається бонус 1% від суми.
2. Для зняття грошей withdraw дозволяється перевищувати баланс (овердрафт до 
1000).
3. Для переведення коштів transfer додається комісія 0.5%.
Приклад завдання:
• Створіть об'єкт PremiumAccount і звичайний BankAccount.
• Виконайте операції поповнення, зняття та переказів для обох типів рахунків.
• Порівняйте результати"""

# 6
print("*** Task 6 ***")
User6 = BankAccount("Eugen", 300)
User7 = PremiumAccount("Dmyitro", True, 300)
print(User6, User7)
User6.deposit(1000)
User7.deposit(1000)
print(User6, User7)
User6.withdraw(500)
User7.withdraw(500)
print(User6, User7)
User6.transfer(300, User7, "Transfer")
User7.transfer(300, User6, "Transfer")
print(User6, User7)
User7.withdraw(1000)
print(User6, User7)