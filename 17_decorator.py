# Decorators in Python

# A decorator is a function that takes another function as an argument,
# adds some kind of functionality to it, and returns another function.
# The original function remains unchanged.

# The `wrapper` function is defined inside the decorator and wraps around the original function.
# It allows us to run code before and/or after calling the original function.

# Basic Decorator Example

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()


# Decorator with Arguments

def square_decorator(func):
    def wrapper(x):
        result = func(x)
        print(f"Square of {x} is {result}")
    return wrapper

@square_decorator
def square(n):
    return n * n

square(5)


# Multiple Decorators

def decorator1(func):
    def wrapper():
        print("Decorator 1 before")
        func()
        print("Decorator 1 after")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 before")
        func()
        print("Decorator 2 after")
    return wrapper

@decorator1
@decorator2
def show():
    print("Inside show function")

show()


# Using functools.wraps to preserve function metadata

from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function metadata preserved")
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def say_hello():
    """This function says hello"""
    print("Hello")

print(say_hello.__name__)
print(say_hello.__doc__)
say_hello()


# Decorator for authentication check

def authenticate(func):
    def wrapper(user):
        if user == "admin":
            print("Access granted")
            func(user)
        else:
            print("Access denied")
    return wrapper

@authenticate
def dashboard(user):
    print(f"Welcome to dashboard, {user}")

dashboard("admin")
dashboard("guest")


"""
In this file, we covered:
- What decorators are and how they work
- What the 'wrapper' function does inside decorators
- Creating basic and argument-based decorators
- Stacking multiple decorators
- Using functools.wraps to preserve metadata like __name__ and __doc__
- Practical example: authentication check using decorators
"""
