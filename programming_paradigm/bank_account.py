# A simple bank script to perform banking operations

class BankAccount:
    def __init__(self, account_balance):
        account_balance = 0
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        else:
            self.account_balance -= amount
            return True
        
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"