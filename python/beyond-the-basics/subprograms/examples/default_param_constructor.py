class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

a = BankAccount("Herman")
b = BankAccount("Farah", 1000)

print(a.balance) # 0
print(b.balance) # 1000