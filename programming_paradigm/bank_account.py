## Author: here

class BankAccount:

    def __init__(self, account_balance: float):
        self.account_balance = account_balance

    def deposit(self, amount: float):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount: float):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return self.account_balance
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

