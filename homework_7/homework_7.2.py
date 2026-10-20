class ATM:
    def __init__(self, banknote20, banknote50, banknote100):
        self.banknote20 = banknote20
        self.banknote50 = banknote50
        self.banknote100 = banknote100

    def add_money(self, banknote20, banknote50, banknote100):
        self.banknote20 += banknote20
        self.banknote50 += banknote50
        self.banknote100 += banknote100

    def withdraw(self, amount):
        for count100 in range(min(amount // 100, self.banknote100), -1, -1):
            remainder_after_100 = amount - count100 * 100

            for count50 in range(
                min(remainder_after_100 // 50, self.banknote50), -1, -1
            ):
                remainder = remainder_after_100 - count50 * 50

                if remainder % 20 == 0:
                    count20 = remainder // 20

                    if count20 <= self.banknote20:
                        self.banknote100 -= count100
                        self.banknote50 -= count50
                        self.banknote20 -= count20

                        print(
                            f"Выдано купюр: 100 — {count100}, "
                            f"50 — {count50}, 20 — {count20}"
                        )
                        return True

        print(f"Сумму {amount} выдать невозможно.")
        return False

    def show_info(self):
        print(
            f"Остаток: купюр по 20 — {self.banknote20}, "
            f"по 50 — {self.banknote50}, "
            f"по 100 — {self.banknote100}"
        )


atm = ATM(5, 3, 2)
atm.add_money(2, 10, 20)

atm.withdraw(170)
atm.withdraw(80)
atm.withdraw(777)
atm.withdraw(1000)
atm.withdraw(10000)

atm.show_info()