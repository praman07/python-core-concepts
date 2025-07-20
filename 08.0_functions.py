"""
This file covers Python Functions including:
- How to define and call functions
- Function parameters and arguments
- Default and keyword arguments
- Return values
- Local vs global scope
- Use of pass, return, and None
"""

# Defining and calling a simple function
def greet():
    print("Welcome to Python Functions!")

greet()


# Function with parameters and arguments
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Praman")


# Function with multiple parameters
def add(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add(5, 10)


# Function with return value
def subtract(x, y):
    return x - y

result = subtract(15, 8)
print(f"Subtraction result: {result}")


# Function with default arguments
def power(base, exponent=2):
    return base ** exponent

print(f"Power (default exponent): {power(5)}")
print(f"Power (custom exponent): {power(2, 5)}")


# Keyword arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(age=21, city="Delhi", name="Aman")


# Using return without value (returns None)
def nothing():
    return

x = nothing()
print(f"Return value of nothing(): {x}")


# Use of 'pass' (placeholder for future code)
def future_function():
    pass


# Global vs Local Scope

count = 10  # Global variable

def show_scope():
    count = 5  # Local variable (shadows global)
    print(f"Inside function, count = {count}")

show_scope()
print(f"Outside function, count = {count}")


# Using 'global' keyword to modify global variable
score = 0

def increase_score():
    global score
    score += 10
    print(f"Score inside function: {score}")

increase_score()
print(f"Score outside function: {score}")


"""
What we have done in this file:
Explained function declaration and calling
Worked with parameters, return values, and default arguments
Used keyword arguments for readability
Demonstrated local and global variable scope
Used pass and return (including returning None)
"""
