class BankAccount:
    def __init__ (self,account_balance):
        self.account_balance = account_balance
        account_balance = 0
    def deposit(self, amount):
        account_balance = account_balance + amount
    def withdaraw(self, amount):
        account_balance -= amount
    def diaplay_balace():
        print('Your current balance is ',account_balance)
