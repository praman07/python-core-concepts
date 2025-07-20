"""
This file covers custom implementations of common math functions:
- factorial
- gcd (Greatest Common Divisor)
- lcm (Least Common Multiple)
- is_prime (check prime)
- sqrt (square root using Newton's method)
- floor (round down)
- ceil (round up)
- exp (exponential function)
- log (natural logarithm)
- sin (sine function)
"""

# Factorial (n!)
def factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# Greatest Common Divisor using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# Least Common Multiple using gcd
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Square root using Newton's method
def sqrt(number, tolerance=1e-10):
    if number < 0:
        raise ValueError("sqrt() not defined for negative numbers")
    if number == 0:
        return 0
    guess = number
    while True:
        next_guess = 0.5 * (guess + number / guess)
        if abs(guess - next_guess) < tolerance:
            return next_guess
        guess = next_guess


# Floor function (round down)
def floor(number):
    int_part = int(number)
    if number >= 0 or number == int_part:
        return int_part
    else:
        return int_part - 1


# Ceil function (round up)
def ceil(number):
    int_part = int(number)
    if number <= 0 or number == int_part:
        return int_part
    else:
        return int_part + 1


# Exponential function e^x using Taylor series
def exp(x, terms=20):
    result = 1.0  # first term
    numerator = 1.0
    denominator = 1.0
    for n in range(1, terms):
        numerator *= x
        denominator *= n
        result += numerator / denominator
    return result


# Natural logarithm ln(x) using series expansion around 1
def log(x, terms=100):
    if x <= 0:
        raise ValueError("log() undefined for non-positive values")
    y = (x - 1) / (x + 1)
    y_power = y
    result = 0.0
    for n in range(terms):
        term = y_power / (2 * n + 1)
        result += term
        y_power *= y * y
    return 2 * result


# Sine function sin(x) using Taylor series (x in radians)
def sin(x, terms=10):
    result = 0.0
    sign = 1
    power = x
    factorial_den = 1
    for n in range(terms):
        term = sign * power / factorial_den
        result += term
        sign *= -1
        power *= x * x
        factorial_den *= (2 * n + 2) * (2 * n + 3)
    return result


# Examples and testing
print(f"factorial(6): {factorial(6)}")  # 720
print(f"gcd(48, 18): {gcd(48,18)}")  # 6
print(f"lcm(12, 15): {lcm(12,15)}")  # 60
print(f"is_prime(37): {is_prime(37)}")  # True
print(f"sqrt(25): {sqrt(25)}")  # 5.0
print(f"floor(3.9): {floor(3.9)}")  # 3
print(f"ceil(3.1): {ceil(3.1)}")  # 4
print(f"exp(1): {exp(1)}")  # approx e=2.71828
print(f"log(2): {log(2)}")  # approx 0.6931
print(f"sin(3.141592/2): {sin(3.141592/2)}")  # approx 1.0

"""
What we have done in this file:
- Implemented key math functions: factorial, gcd, lcm, is_prime, sqrt, floor, ceil, exp, log, sin
- Used series expansions for exp, log, and sin
- Provided example usages to demonstrate correctness
"""
