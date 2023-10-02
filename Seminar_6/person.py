from bank import Bank


class Person:

    def __init__(self):
        self.balance = 0.0

    def add_money(self, money: float) -> None:
        self.balance += money

    def transfer_money(self, bank: Bank, money: float):
        if self.balance >= money > 0:
            bank.receive_money(money)
            self.balance -= money
        else:
            raise ValueError('Problem with your money or balance')
