
# What is a constructor?
# A constructor is a special method called automatically when an object is created.
# In Python, the constructor method is named __init__.

# Example 1: Basic Constructor
class Car:
    def __init__(self):
        print("Car constructor called")

car1 = Car()


# Example 2: Parameterized Constructor
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}\nRoll No: {self.roll_no}")

s1 = Student("Praman", 1536)
s1.display()


# Example 3: Constructor with Default Arguments (to mimic multiple constructors)
class Laptop:
    def __init__(self, brand="Unknown", ram="8GB"):
        self.brand = brand
        self.ram = ram

    def specs(self):
        print(f"Brand: {self.brand}\nRAM: {self.ram}")

l1 = Laptop("Dell", "16GB")
l2 = Laptop()  # Uses default values
l1.specs()
l2.specs()


# Example 4: Constructor in Inheritance
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        print(f"Engine with {self.horsepower} HP initialized")

class SportsCar(Engine):
    def __init__(self, horsepower, brand):
        super().__init__(horsepower)  # Call parent class constructor
        self.brand = brand
        print(f"SportsCar of brand {self.brand} initialized")

sc = SportsCar(670, "Ferrari")


# Example 5: Using @classmethod to mimic constructor overloading
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title.strip(), author.strip())

    def details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

b1 = Book("1984", "George Orwell")
b2 = Book.from_string("The Alchemist - Paulo Coelho")
b1.details()
b2.details()


# Example 6: Destructor
# The destructor method __del__ is called when an object is about to be destroyed

class Demo:
    def __init__(self):
        print("Constructor: Object is created")

    def __del__(self):
        print("Destructor: Object is being destroyed")

d = Demo()
del d  # Destructor is called explicitly when object is deleted

"""
In this file, we covered:
- __init__() constructor method
- Default constructors
- Parameterized constructors
- Default arguments to simulate overloading
- Constructors with inheritance and super()
- Using @classmethod to define alternate constructors
- __del__() destructor method to handle object cleanup
"""
