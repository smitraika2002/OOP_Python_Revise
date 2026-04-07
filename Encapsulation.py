class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public attribute
        self.__balance = balance        # Private attribute

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Public method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    # Public method to check balance
    def get_balance(self):
        return self.__balance

    # Private method
    def __log_transaction(self, message):
        print(f"[LOG]: {message}")


# Creating object (instance)
account1 = BankAccount("Smit", 500)

# Using public methods
account1.deposit(200)
account1.withdraw(100)

# Printing balance
print("Current Balance:", account1.get_balance())