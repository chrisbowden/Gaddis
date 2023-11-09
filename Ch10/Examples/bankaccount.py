# This program simulates a bank account

class BankAccount:
    # The __init__ method accepts an argument for
    # the account balance. It is assigned to
    # the __balance attribute

    def __init__(self, bal):
        self.__balance == bal

    # The deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    # from the account
