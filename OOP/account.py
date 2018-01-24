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

class Checking_Account(Account):
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking_Account("balance.txt", 3)
checking.transfer(10)
print(checking.balance)
checking.commit_changes()
