class CheckingAccount:
    def __init__(self, bal):
        self.__balance=bal
    def deposit(self, amount):
        self.__balance+=amount
    def withdraw(self, amount):
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            print('Insufficient funds')
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f'Your balance is ${self.__balance:,.2f}'
def main():
    bal=float(input('Starting balance:   '))
    checking=CheckingAccount(bal)
    check=float(input('How much would you like to deposit?   '))
    print('Amount being deposited into your account')
    checking.deposit(check)
    print(f'Your balance is {checking.get_balance():,.2f}.')
    cash=float(input('How much would you like to withdraw?   '))
    print('Amount being withdrawn from your account')
    checking.withdraw(cash)
    print(f'Your balance is {checking.get_balance():,.2f}.')
main()
            
    
    
