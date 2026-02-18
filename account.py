class BankAccount:
    def __init__(self, name, pin, balance=0, history=None):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = history if history else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")
            return "Deposit successful"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.history.append(f"Withdrawn ₹{amount}")
        return "Withdrawal successful"

    def check_balance(self):
        return self.balance

    def get_history(self):
        return self.history
