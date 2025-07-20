# Abstraction is the process of hiding complex implementation details
# and showing only the necessary features of an object.

# In Python, abstraction is achieved using abstract classes and methods from the 'abc' module.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def fuel_type(self):
        print("Most vehicles run on petrol, diesel, or electricity.")

# Concrete class that implements abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine roars to life")

    def stop_engine(self):
        print("Motorcycle engine shut down")

c = Car()
c.start_engine()
c.stop_engine()
c.fuel_type()

m = Motorcycle()
m.start_engine()
m.stop_engine()

# Trying to instantiate an abstract class directly would raise an error
# v = Vehicle()  # This will raise TypeError

# Summary:
# - Abstraction focuses on what an object does, not how it does it.
# - Abstract classes cannot be instantiated.
# - Abstract methods must be implemented in child classes.
# - Helps in defining a blueprint for other classes.
