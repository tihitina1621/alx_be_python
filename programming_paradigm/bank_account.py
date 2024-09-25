class BankAccount:
    def __init__ (self,account_balance):
        self.account_balance = account_balance
        account_balance = 0
    def deposit(self, amount):
        account_balance = account_balance + amount
    def withdraw(self, amount):
        account_balance -= amount
    def display_balance():
        print('Current Balance: ',account_balance)
