class Account:
    def __init__(self, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")

# Create an instance of Account and interact with balance
account = Account(1000)
print(account.get_balance())  # Get balance
account.set_balance(500)  # Set new balance
print(account.get_balance())
