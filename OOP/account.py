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
    #doc string
    """
    This class generates checking account
    """
    type="checking" # class variable. Shared among all instances of the class

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# inheritance text
checking = Checking_Account("balance.txt", 3)
checking.transfer(10)
print(checking.balance)
checking.commit_changes()

# glosary
acc1_checking = Checking_Account("acc1.txt", 1)
print(acc1_checking.balance) #instance variable
print(acc1_checking.type) # class variable
print(acc1_checking.__doc__) # doc string

acc2_checking = Checking_Account("acc2.txt", 1)
print(acc2_checking.balance) #instance variable
print(acc1_checking.type) # class variable
