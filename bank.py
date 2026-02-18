import json
from account import BankAccount

DATA_FILE = "data.json"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def create_account(self, name, pin, balance=0):
        if name in self.accounts:
            return "Account already exists"
        self.accounts[name] = BankAccount(name, pin, balance)
        self.save_data()
        return "Account created successfully"

    def login(self, name, pin):
        account = self.accounts.get(name)
        if account and account.pin == pin:
            return account
        return None

    def save_data(self):
        data = {}
        for name, acc in self.accounts.items():
            data[name] = {
                "pin": acc.pin,
                "balance": acc.balance,
                "history": acc.history
            }

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)

            for name, info in data.items():
                self.accounts[name] = BankAccount(
                    name,
                    info["pin"],
                    info["balance"],
                    info["history"]
                )
        except FileNotFoundError:
            pass
