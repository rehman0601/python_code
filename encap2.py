class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

# Test the class
account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
account.set_balance(1500)
print(f"New Balance: {account.get_balance()}")
account.set_balance(-500)  # Invalid amount
