class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())

    def commit_changes(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

acc = Account("balance.txt")
print(acc.balance)
acc.withdraw(100)
acc.commit_changes()
print(acc.balance)
acc.deposit(500)
acc.commit_changes()
print(acc.balance)
