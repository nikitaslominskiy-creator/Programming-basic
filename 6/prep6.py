class BankAccount:
    def __init__(self, owner, balance =0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough mmoney on balance")
            return
        self.balance -= amount

    def describe(self):
        return f"{self.owner}: {self.balance:.2f} Kč"

acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)       
print(acc.describe()) 

