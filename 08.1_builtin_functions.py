"""
This file covers custom implementations of common built-in functions:
- min()
- max()
- abs()
- round()
- pow()
- avg()  # average, not built-in but commonly used
"""

# Custom implementation of min() function
def custom_min(iterable):
    """Return the smallest item in the iterable."""
    smallest = iterable[0]
    for item in iterable[1:]:
        if item < smallest:
            smallest = item
    return smallest


# Custom implementation of max() function
def custom_max(iterable):
    """Return the largest item in the iterable."""
    largest = iterable[0]
    for item in iterable[1:]:
        if item > largest:
            largest = item
    return largest


# Custom implementation of abs() function
def custom_abs(number):
    """Return the absolute value of a number."""
    if number < 0:
        return -number
    return number


# Custom implementation of round() function
def custom_round(number, digits=0):
    """
    Round a number to a given precision in decimal digits (default 0 digits).
    This mimics Python's built-in round() for positive digits.
    """
    multiplier = 10 ** digits
    # Shift decimal point, add 0.5 for rounding, then floor (int truncation)
    shifted = number * multiplier
    if shifted >= 0:
        shifted = int(shifted + 0.5)
    else:
        shifted = int(shifted - 0.5)
    return shifted / multiplier


# Custom implementation of pow() function
def custom_pow(base, exponent):
    """
    Return base raised to the power of exponent.
    Handles integer exponents only (positive, zero, negative).
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / custom_pow(base, -exponent)
    else:
        result = 1
        for _ in range(exponent):
            result *= base
        return result


# Custom implementation of avg() function (not built-in)
def custom_avg(iterable):
    """Return the average (arithmetic mean) of numeric items in the iterable."""
    total = 0
    count = 0
    for item in iterable:
        total += item
        count += 1
    if count == 0:
        raise ValueError("custom_avg() arg is an empty iterable")
    return total / count


# Examples and testing
numbers = [12, 4, -56, 7, 34, -8]

print(f"custom_min: {custom_min(numbers)}")
print(f"built-in min: {min(numbers)}")

print(f"custom_max: {custom_max(numbers)}")
print(f"built-in max: {max(numbers)}")

print(f"custom_abs(-10): {custom_abs(-10)}")
print(f"built-in abs(-10): {abs(-10)}")

print(f"custom_round(3.14159, 2): {custom_round(3.14159, 2)}")
print(f"built-in round(3.14159, 2): {round(3.14159, 2)}")

print(f"custom_pow(2, 5): {custom_pow(2, 5)}")
print(f"built-in pow(2, 5): {pow(2, 5)}")

print(f"custom_pow(2, -3): {custom_pow(2, -3)}")
print(f"built-in pow(2, -3): {pow(2, -3)}")

print(f"custom_avg(numbers): {custom_avg(numbers)}")

"""
What we have done in this file:
- Implemented custom versions of min, max, abs, round, pow, and avg functions
- Compared outputs with built-in Python functions for verification
- Explained basic algorithmic approach for each function
"""
