
# Polymorphism means "many forms". In Python, it allows us to define methods in the child class
# with the same name as defined in their parent class. It also allows functions to work with objects
# of different types as long as they support the expected method or operation.

# Example 1: Polymorphism with Functions and Classes
class Ferrari:
    def fuel_type(self):
        return "Petrol"

class Tesla:
    def fuel_type(self):
        return "Electric"

def print_fuel(car):
    print(car.fuel_type())

f8 = Ferrari()
model_s = Tesla()

print_fuel(f8)
print_fuel(model_s)

# Example 2: Method Overriding
# Child class overrides a method from the parent class

class Car:
    def start(self):
        print("Starting the car...")

class MercedesG63(Car):
    def start(self):
        print("Starting the Mercedes G63 with V8 engine...")

vehicle = MercedesG63()
vehicle.start()

# Example 3: Duck Typing in Python
# If an object walks like a duck and quacks like a duck, it is treated as a duck

class Ferrari:
    def speed(self):
        print("Ferrari top speed is 350 km/h")

class FordGT:
    def speed(self):
        print("Ford GT top speed is 347 km/h")

def show_speed(car):
    car.speed()

f8 = Ferrari()
gt = FordGT()

show_speed(f8)
show_speed(gt)

"""
In this file, we covered:
- Polymorphism through same method names in different classes
- Method overriding: redefining a method in a subclass
- Duck typing: if an object has the required method, it can be passed (regardless of class)
"""
