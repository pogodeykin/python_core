class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств на карте")

    def show_info(self):
        print(f"Номер счёта: {self.account_number}, баланс: {self.balance:.2f}")



SBER = CreditCard("123456", 1000)
VTB = CreditCard("234567", 2500)
ALFA = CreditCard("345678", 5000)


SBER.deposit(300)
VTB.deposit(500)
ALFA.withdraw(1200)


SBER.show_info()
VTB.show_info()
ALFA.show_info()