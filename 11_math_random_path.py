"""
This file demonstrates:
- Built-in Python math functions using the math module
- Random number and sequence generation using the random module
- Basic file system operations using pathlib and os modules
"""

# MATH MODULE
import math

# Constants
print(f"Value of PI: {math.pi}")
print(f"Value of e: {math.e}")

# Basic math functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Power: 2^3 = {math.pow(2, 3)}")
print(f"Ceiling of 5.3: {math.ceil(5.3)}")
print(f"Floor of 5.8: {math.floor(5.8)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Log base 10 of 1000: {math.log10(1000)}")
print(f"Sine of 90 degrees: {math.sin(math.radians(90))}")

# RANDOM MODULE
import random

# Random integers
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")

# Random float between 0 and 1
print(f"Random float between 0 and 1: {random.random()}")

# Random choice from a list
colors = ["red", "green", "blue", "yellow"]
print(f"Random color: {random.choice(colors)}")

# Shuffle a list
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(f"Shuffled list: {nums}")

# Sample without replacement
print(f"Random sample of 3 items: {random.sample(colors, 3)}")

# OS and PATHLIB MODULES
import os
from pathlib import Path

# Current working directory
print(f"Current working directory (os): {os.getcwd()}")

# Creating a new directory using os (won't raise error if exists)
dir_name = "example_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Created directory: {dir_name}")
else:
    print(f"Directory already exists: {dir_name}")

# Pathlib for cleaner path handling
path = Path("example_folder") / "file.txt"
print(f"Constructed path using pathlib: {path}")

# Create and write to file using pathlib
path.write_text("This file was created using pathlib in Python.")
print(f"Contents written to: {path}")

# Read the contents
contents = path.read_text()
print(f"File contents: {contents}")

# Delete file
if path.exists():
    path.unlink()
    print("Deleted the file using pathlib.")

# Delete directory
if path.parent.exists():
    os.rmdir(path.parent)
    print("Deleted the directory using os.")

"""
What we have done in this file:
- Used the math module for constants and math operations
- Demonstrated random module functions like randint, choice, shuffle, and sample
- Used os and pathlib to work with directories and files safely and efficiently
"""

