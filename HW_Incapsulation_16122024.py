"""Доробити клас свого банку
(Додати ще деякі атрибути, та методи тощо)"""

from uuid import uuid4


class UserBank:
    def __init__(self, name, surname, age, logPhone, password='', email=''):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__guid = str(uuid4())
        self.__balance = 0
        self.__loginPhone = logPhone
        self.__email = email
        if password == '':
            self.__password = self.getPassword()
        else:
            self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, newSurname):
        self.__surname = newSurname

    @property
    def loginPhone(self):
        return self.__loginPhone

    @loginPhone.setter
    def loginPhone(self, newNumber):
        if newNumber.lower().startswith("+380") and not newNumber.isalpha() and len(newNumber) == 13:
            self.__loginPhone = newNumber
        else:
            print("Введено не коректний номер!")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newEmail):
        if '@' in newEmail and '.' in newEmail:
            self.__email = newEmail
        else:
            print("Введено не коректний email!")

    @property
    def balance(self):
        return self.__balance

    @property
    def password(self):
        return self.__password

    def changePass(self):
        answ = input("Enter old password: ")
        if answ == self.__password:
            while True:
                new_pass1 = input("Enter new password: ")
                new_pass2 = input("Confirm u pass: ")
                if new_pass1 == new_pass2:
                    self.__password = new_pass1
                    print("Your password has been changed!")
                    break

    def getPassword(self):
        password = str(uuid4())
        return password[0:8]

    def showInfo(self):
        print(f"{'-' * 21}\n"
              f"Name: {self.__name}\n"
              f"Surname: {self.__surname}\n"
              f"Phone: {self.__loginPhone}\n"
              f"Email: {self.__email}\n"
              f"Balance: {self.__balance}\n"
              f"{'-' * 21}")

    def sendMoney(self, sender, money=0):
        money = abs(money)
        sender.__balance += money
        self.__balance -= money

    def depositMoney(self, money):
        money = abs(money)
        if money > 0:
            self.__balance += money

    def withdrawMoney(self, money):
        money = abs(money)
        if money > 0 and money <= self.__balance:
            self.__balance -= money
        else:
            print(f"Withdraw money error!")


while True:
    name = input(f"Enter name: ")
    if name == "":
        print("Name cannot be empty!")
        continue
    surname = input(f"Enter surname: ")
    if surname == "":
        print("Surname cannot be empty!")
        continue
    age = int(input(f"Enter age: "))
    if age < 18 or age > 65:
        print("Age must be between 18 and 65!")
        continue
    phone_number = input(f"Enter phone number: ")
    if not phone_number.lower().startswith("+380") and not phone_number.isalpha() and len(phone_number) != 13:
        print(f"Input phone number at format \"+380123456789\"")
        continue
    pwd = input(f"Enter password: ")
    email = input(f"Enter email: ")
    break

NewUser = UserBank(name, surname, age, phone_number, pwd, email)
NewUser.showInfo()
while True:
    user_menu = input(f"{str("---Menu---").rjust(17)}\n"
                      f"1. Account parameters\n"
                      f"2. Bank operations\n"
                      f"3. Show information\n"
                      f"4. Exit\n")
    if user_menu.startswith("1"):
        while True:
            user_choice_menu = input(f"{str("---Account---").rjust(17)}\n"
                                     f"1. Change Name\n"
                                     f"2. Change Surname\n"
                                     f"3. Change Age\n"
                                     f"4. Change Phone\n"
                                     f"5. Change Email\n"
                                     f"6. Show Password\n"
                                     f"7. Change Password\n"
                                     f"8. Main Menu\n")
            if user_choice_menu.startswith("1"):
                newName = input("Enter new name: ")
                if newName != "":
                    NewUser.name = newName
                else:
                    print(f"Name error!")
                    continue
            elif user_choice_menu.startswith("2"):
                newSurname = input("Enter new surname: ")
                if newSurname != "":
                    NewUser.surname = newSurname
                else:
                    print(f"Surname error!")
                    continue
            elif user_choice_menu.startswith("3"):
                newAge = input("Enter new age: ")
                if newAge != 0:
                    NewUser.age = newAge
                else:
                    print(f"Age error!")
                    continue
            elif user_choice_menu.startswith("4"):
                newPhone = input("Enter new phone: ")
                if newPhone != "":
                    NewUser.loginPhone = newPhone
                else:
                    print(f"Phone error!")
                    continue
            elif user_choice_menu.startswith("5"):
                newEmail = input("Enter new email: ")
                if newEmail != "":
                    NewUser.email = newEmail
                else:
                    print(f"Email error!")
                    continue
            elif user_choice_menu.startswith("6"):
                print(f"Your password: {NewUser.password}")
            elif user_choice_menu.startswith("7"):
                NewUser.changePass()
            elif user_choice_menu.startswith("8"):
                break
            else:
                print("Invalid option!")
                continue
    elif user_menu.startswith("2"):
        while True:
            user_operation_menu = input(f"{str("---Operations---").rjust(17)}\n"
                                        f"1. Deposit money\n"
                                        f"2. Withdraw money\n"
                                        f"3. Exit\n")
            if user_operation_menu.startswith("1"):
                sum_deposit = int(input("Input deposit: "))
                if sum_deposit > 0:
                    NewUser.depositMoney(sum_deposit)
                    print(f"Deposit money successfully added!\n"
                          f"Your balance: {NewUser.balance}")
                else:
                    print(f"Deposit error!")
                    continue
            elif user_operation_menu.startswith("2"):
                sum_withdraw = int(input("Input withdraw: "))
                if sum_withdraw > 0:
                    NewUser.withdrawMoney(sum_withdraw)
                    print(f"Withdraw money success!\n"
                          f"Your balance: {NewUser.balance}")
                else:
                    print(f"Withdraw error!")
                    continue
            elif user_operation_menu.startswith("3"):
                break
            else:
                print("Invalid option!")
                continue
    elif user_menu.startswith("3"):
        NewUser.showInfo()
    elif user_menu.startswith("4"):
        print("Have a nice day!")
        break
    else:
        print("Invalid option!")
        continue
