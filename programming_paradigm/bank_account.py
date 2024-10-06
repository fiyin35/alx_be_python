# Author: Fiyinfolu
# Bank Account class with method
# deposit to deposit amount specify by user
# provided the amount is greater than zero
# withdraw method to withdraw specify amount from the account
# balance, provided the withdrawal amount is not greater than
# the account_balance
# display_balance simply display the current account balance

class BankAccount:

    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount: float):
        if amount >= 1:
            self.account_balance += amount
        else:
            print("You can not deposit less than or equal to zero")
        return float(self.account_balance)

    def withdraw(self, amount: float):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return float(self.account_balance)
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

