class Bank:

    def __init__(self):
        self.repo = 0.0

    def receive_money(self, money: float) -> None:
        self.repo += money
