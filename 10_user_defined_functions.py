"""
This file covers:
- How to define and use user-defined functions in Python
- Use of parameters, return values
- Positional and keyword arguments
- Default arguments
- Nested functions
- Basic function design examples
"""

# Function with no parameters and no return value
def greet():
    print("Hello, welcome to Python!")

greet()

# Function with parameters
def add(a, b):
    result = a + b
    print(f"Sum: {result}")

add(10, 20)

# Function with return value
def square(x):
    return x * x

value = square(5)
print(f"Square of 5 is: {value}")

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(f"5^2 with default: {power(5)}")
print(f"5^3: {power(5, 3)}")

# Keyword arguments
def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info(course="AI", name="John", age=20)

# Nested functions
def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()

outer()

# Function returning multiple values
def calc(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else None

s, d, m, q = calc(10, 2)
print(f"Sum: {s}, Diff: {d}, Mul: {m}, Div: {q}")

# Checking even or odd using a function
def is_even(num):
    return num % 2 == 0

print(f"8 is even: {is_even(8)}")
print(f"7 is even: {is_even(7)}")

# Prime check using a function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"5 is prime: {is_prime(5)}")
print(f"10 is prime: {is_prime(10)}")

# Factorial using a function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of 5 is: {factorial(5)}")


"""
What we have done in this file:
- Created functions with and without parameters
- Used return values including multiple return values
- Demonstrated positional, keyword, and default arguments
- Explained nested functions and basic real examples like factorial and prime check
"""
