class Account:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def withdraw(self, amount):
        self.balance = self.balance - abs(amount)

    def deposit(self, amount):
        self.balance = self.balance + amount


ac = Account(1000)
ac.deposit(2000)
ac.withdraw(-1000)
print(ac.balance)
