# CLASS AND OBJECTS IN PYTHON

# A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions).
# An object is an instance of a class.

# Defining a simple class
class Car:
    def __init__(self, brand, model):
        self.brand = brand          # instance attribute
        self.model = model          # instance attribute

    def start_engine(self):         # instance method
        print(f"{self.brand} {self.model} engine started.")

# Creating objects (instances) of the Car class
car1 = Car("Ferrari", "F8")
car2 = Car("Ford", "GT")

# Accessing attributes and methods
print(f"Car 1 brand: {car1.brand}")
print(f"Car 2 model: {car2.model}")

car1.start_engine()
car2.start_engine()


# CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES

class Dog:
    species = "Canine"  # class attribute (shared across all instances)

    def __init__(self, name, age):
        self.name = name     # instance attribute
        self.age = age       # instance attribute

dog1 = Dog("Max", 4)
dog2 = Dog("Bella", 2)

print(f"{dog1.name} is a {dog1.species} aged {dog1.age}")
print(f"{dog2.name} is a {dog2.species} aged {dog2.age}")


# OBJECT BEHAVIOR

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def upgrade_ram(self, new_ram):
        self.ram = new_ram

    def specs(self):
        print(f"Laptop brand: {self.brand}, RAM: {self.ram}GB")

l1 = Laptop("Dell", 8)
l1.specs()
l1.upgrade_ram(16)
l1.specs()


# DELETING OBJECTS

class Temporary:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")

temp = Temporary()
del temp


"""
In this file, we covered:
- What classes and objects are
- How to define a class and create objects
- Instance attributes and methods
- Class attributes (shared across all instances)
- Example of object behavior using methods
- Deleting objects using del and destructor (__del__)
"""
