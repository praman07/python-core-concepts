# Encapsulation is the concept of hiding internal data and only exposing access through methods.
# It allows controlled access to the attributes using public, protected, and private access modifiers.

# Public Members
class Car:
    def __init__(self, brand, model):
        self.brand = brand          # Public attribute
        self.model = model          # Public attribute

    def show(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Ferrari", "812 Superfast")
car1.show()
print(car1.brand)  # Accessible directly (public)

# Protected Members
class Engine:
    def __init__(self, cylinders):
        self._cylinders = cylinders   # Protected attribute (convention)

    def _status(self):               # Protected method (convention)
        print(f"Engine has {self._cylinders} cylinders")

e1 = Engine(12)
print(e1._cylinders)    # Accessible but discouraged
e1._status()            # Can be accessed but is intended for internal use

# Private Members
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"{self.owner}'s balance is ₹{self.__balance}")

account1 = BankAccount("Praman", 50000)
account1.deposit(10000)
account1.withdraw(20000)
account1.show_balance()

# Trying to access private variable directly
# print(account1.__balance)        # This would raise an AttributeError
print(account1._BankAccount__balance)  # Name mangling allows access (not recommended)

# Getters and Setters using methods
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks

s1 = Student()
s1.set_marks(95)
print(s1.get_marks())

# Getters and Setters using @property decorator
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative")

p1 = Product(1000)
print(p1.price)
p1.price = 1500
print(p1.price)
p1.price = -500  # Will print error and not update

# Summary:
# - Public: accessible from anywhere
# - Protected: accessible but intended for internal/subclass use
# - Private: not directly accessible (name mangling applies)
# - Getters and Setters control access to private attributes
