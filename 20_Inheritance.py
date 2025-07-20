# INHERITANCE IN PYTHON
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
# It promotes code reuse and logical hierarchy.

# SINGLE INHERITANCE
class FactoryMumbai:
    a = "I am a variable defined in the parent class (FactoryMumbai)"
    
    def hello(self):
        print("I am a method defined inside the parent class")

class FactoryPune(FactoryMumbai):
    pass

obj = FactoryMumbai()
obj1 = FactoryPune()
obj1.hello()  # Inherited method from parent


# SINGLE INHERITANCE with constructor and super()
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model
    
    def details(self):
        return f"Brand: {self.brand}\nColor: {self.color}\nModel: {self.model}"

car12 = Car("Ferrari", "Red", "2012")
print(car12.details())


# METHOD OVERRIDING IN INHERITANCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRoll No: {self.roll_no}")

st1 = Student("Praman", 20, 1536)
st1.show_info()


# MULTILEVEL INHERITANCE
class Porsche:
    def __init__(self):
        print("Porsche 911")

class P911(Porsche):
    def __init__(self):
        super().__init__()

class EV(P911):
    def __init__(self):
        super().__init__()

ui = EV()


class Legacy:
    def __init__(self, brand):
        self.brand = brand

class Interval(Legacy):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Final(Interval):
    def __init__(self, brand, model, topspeed):
        super().__init__(brand, model)
        self.topspeed = topspeed
    
    def show_details(self):
        print(f"\nBrand: {self.brand}\nModel: {self.model}\nTop Speed: {self.topspeed} km/h")

car = Final("Ferrari", "La-Ferrari-Aperta", 340)
car.show_details()


# HIERARCHICAL INHERITANCE
class Car:
    def brand(self):
        print("This is a generic car")

class Ferrari(Car):
    def model(self):
        print("Ferrari F8 Tributo")

class FordGT(Car):
    def model(self):
        print("Ford GT Heritage Edition")

f = Ferrari()
g = FordGT()

f.brand()
f.model()

g.brand()
g.model()


# MULTIPLE INHERITANCE
class Animal:
    def __init__(self, name):
        print("Animal constructor")
        self.name = name

class Human:
    def __init__(self, name, age):
        print("Human constructor")
        self.name = name
        self.age = age

class Robot(Human, Animal):  # MRO: Human → Animal
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Robot constructor\n")

r1 = Robot("AI-Bot", 6)

# Note: If you swap order to (Animal, Human), the Animal's constructor will be used instead.

"""
In this file, we covered:
- What is inheritance and why it's used
- Single inheritance with and without super()
- Method overriding
- Multilevel inheritance
- Hierarchical inheritance
- Multiple inheritance and MRO (Method Resolution Order)
"""
