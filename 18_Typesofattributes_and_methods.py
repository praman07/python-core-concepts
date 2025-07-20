# CLASS ATTRIBUTES
# These are shared among all instances of a class
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand  # Instance attribute

c1 = Car("Ferrari")
c2 = Car("Ford")

print(f"c1 wheels: {c1.wheels}, brand: {c1.brand}")
print(f"c2 wheels: {c2.wheels}, brand: {c2.brand}")

# Changing class attribute affects all instances (unless overridden in instance)
Car.wheels = 6
print(f"After changing class attribute:")
print(f"c1 wheels: {c1.wheels}")
print(f"c2 wheels: {c2.wheels}")


# INSTANCE ATTRIBUTES
# These are unique to each instance
c1.color = "Red"  # Adding an attribute only to c1
print(f"c1 color: {c1.color}")
# print(c2.color)  # This would give an error since c2 has no 'color' attribute


# INSTANCE METHOD
# Works with instance (self)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):  # Instance method
        print(f"Hello, my name is {self.name}")

p1 = Person("Praman")
p1.greet()


# CLASS METHOD
# Works with class, takes 'cls' as first parameter
class Laptop:
    count = 0

    def __init__(self):
        Laptop.count += 1

    @classmethod
    def get_count(cls):  # Class method
        print(f"Total laptops created: {cls.count}")

l1 = Laptop()
l2 = Laptop()
Laptop.get_count()


# STATIC METHOD
# Doesn't take self or cls, behaves like normal function inside a class
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(f"Addition using static method: {Math.add(5, 7)}")

"""
In this file, we covered:
- Class Attributes: shared by all instances (defined outside __init__)
- Instance Attributes: unique to each object (defined in __init__)
- Instance Methods: operate on instances (first parameter is self)
- Class Methods: operate on class (first parameter is cls, use @classmethod)
- Static Methods: utility functions inside class (no self/cls, use @staticmethod)
"""
