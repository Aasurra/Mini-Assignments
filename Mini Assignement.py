#Student Name: Michael Lin
#Student ID: 101484021

class BankAccount:
    def __init__(self, name, balance):
        if len(name) < 10:
            raise ValueError("Name must be at least 10 characters")
        self.name = name
        if balance < 0:
            raise ValueError("Balance must be positive")
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return f"{self.name}: {round(self.balance, 2)}"

    def deposit(self, amount: float):
        if amount < 0:
            print("Amount must be positive")
            return
        self.balance += amount
        self.transactions.append(f"deposit: {round(amount, 2)}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Amount must be greater than balance")
            return
        self.balance -= amount
        self.transactions.append(f"withdraw: {round(amount, 2)}")

    def display_balance(self):
        print(f"Your current balance is: {round(self.balance, 2)}")

    def display_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)