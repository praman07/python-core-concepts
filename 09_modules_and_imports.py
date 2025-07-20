"""
This file covers:
- What modules are in Python
- How to import built-in modules
- Use of math, random, os, pathlib, and abc modules
- Different ways to import (import, from-import, alias)
"""

# Importing the full math module
import math

# Math module functions
print(f"Square root of 25: {math.sqrt(25)}")
print(f"Value of pi: {math.pi}")
print(f"Ceil of 4.1: {math.ceil(4.1)}")
print(f"Floor of 4.9: {math.floor(4.9)}")
print(f"Power: 2^3 = {math.pow(2, 3)}")
print(f"GCD of 20 and 8: {math.gcd(20, 8)}")

# Importing specific functions from random module
from random import randint, choice, shuffle

# Random number between 1 and 10
print(f"Random integer (1 to 10): {randint(1, 10)}")

# Random choice from a list
items = ["apple", "banana", "cherry", "date"]
print(f"Random fruit: {choice(items)}")

# Shuffle a list
shuffle(items)
print(f"Shuffled list: {items}")

# Using os module
import os

# Current working directory
print(f"Current working directory: {os.getcwd()}")

# List all files and folders in current directory
print(f"Files and folders: {os.listdir()}")

# Using pathlib (modern way for path handling)
from pathlib import Path

# Create Path object
path = Path(".")

# List all Python files in current directory
for file in path.glob("*.py"):
    print(f"Python file found: {file.name}")

# dir() shows all attributes of a module
print("Some functions in math module:", dir(math)[:10])

# Using abc module (used for abstraction in OOP)
from abc import ABC, abstractmethod

# Minimal abstract class demo (detailed in abstraction.py)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Note: Cannot create object of Vehicle unless start_engine() is implemented in subclass


"""
What we have done in this file:
- Imported built-in modules: math, random, os, pathlib, and abc
- Used functions like sqrt, ceil, randint, choice, shuffle
- Used both full imports and selective imports
- Inspected module contents using dir()
- Listed files using os and pathlib modules
- Briefly introduced abc module for abstraction (detailed in abstraction.py)
"""
