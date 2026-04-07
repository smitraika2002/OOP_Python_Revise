# Abstraction in Python
# Abstraction is a fundamental concept in object-oriented programming 
# that allows us to hide the complex implementation

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model} engine started.")

#     def stop_engine(self):
#         print(f"{self.make} {self.model} engine stopped.")

# # Creating an instance of the Car class
# my_car = Car("Toyota", "Corolla")
# my_car.start_engine()
# my_car.stop_engine()

# Encapsulation in Python
# Encapsulation is the concept of bundling data (attributes) and methods (functions) 
# that operate on the data into a single unit, typically a class. 
# It also involves restricting access to certain components of an object, 
# which is often achieved through the use of private attributes and methods.

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


# Abstraction means hiding complex implementation details 
# and showing a simple interface to the user.
# The user interacts with methods of the class 
# without knowing how they are implemented.


# Encapsulation means hiding internal data 
# and restricting direct access to it.
# The user can only access data through public methods,
# while private attributes and methods are protected.
