
# Topic: Variables, Data Types, and Typecasting

# Python variables are dynamically typed.
# That means we don't need to declare the type of variable; Python figures it out at runtime.

# Integer
num1 = 10
print(f"Integer value: {num1} | Type: {type(num1)}")

# Float
num2 = 12.23
print(f"Float value: {num2} | Type: {type(num2)}")

# Boolean
for_sale = True
print(f"Boolean value: {for_sale} | Type: {type(for_sale)}")

# String
name = "Python"
print(f"String value: {name} | Type: {type(name)}")

# Complex numbers
# Python supports complex numbers by default using the format: real + imag*j
z = 5 + 2j
print(f"Complex number z: {z}")
print(f"Real part: {z.real}")
print(f"Imaginary part: {z.imag}")
print(f"Type of z: {type(z)}")

# NoneType
# None represents the absence of a value (similar to null in other languages)
empty_var = None
print(f"Value of empty_var: {empty_var}")
print(f"Type of empty_var: {type(empty_var)}")

# Multiple assignment
# Python allows you to assign multiple variables in one line
a, b, c = 1, 2.5, "hello"
print(f"a = {a}, b = {b}, c = {c}")

# Dynamic typing
# Variables can change their type during execution
x = 10
print(f"x is now: {x}, type: {type(x)}")
x = "Now x is a string"
print(f"x is now: {x}, type: {type(x)}")

# id() function
# Returns the memory address (identity) of the object
y = 100
print(f"Value of y: {y}")
print(f"Memory ID of y: {id(y)}")

# Constants in Python
# Python does not have true constants, but by convention, we use uppercase names
MAX_CONNECTIONS = 10
PI = 3.14159
print(f"MAX_CONNECTIONS = {MAX_CONNECTIONS}, PI = {PI}")

# isinstance() function
# Checks if a variable is of a specific type
print(isinstance(num1, int))      # True
print(isinstance(num2, float))    # True
print(isinstance(name, str))      # True
print(isinstance(z, complex))     # True
print(isinstance(for_sale, bool)) # True

# Typecasting: converting one type to another

# float to int
score = 87.6
score_as_int = int(score)  # Decimal part is removed
print(f"Float: {score} → Int: {score_as_int}")

# int to float
value = 15
value_float = float(value)
print(f"Int: {value} → Float: {value_float}")

# string to int
num_str = "123"
converted = int(num_str)
print(f"String: '{num_str}' → Int: {converted}")

# string to float
f_str = "99.99"
converted_float = float(f_str)
print(f"String: '{f_str}' → Float: {converted_float}")

# int to string
n = 101
n_str = str(n)
print(f"Int: {n} → String: '{n_str}'")

# bool to int
# True → 1, False → 0
print(f"True as int: {int(True)}")
print(f"False as int: {int(False)}")

# int to bool
print(f"0 as bool: {bool(0)}")        # False
print(f"Any non-zero number as bool: {bool(5)}")  # True

# float to bool
print(f"0.0 as bool: {bool(0.0)}")    # False
print(f"Non-zero float as bool: {bool(1.23)}")  # True

# string to bool
print(f"Empty string as bool: {bool('')}")  # False
print(f"Non-empty string as bool: {bool('Python')}")  # True

# bool to string
b = False
b_str = str(b)
print(f"Boolean: {b} → String: '{b_str}'")

# Attempting invalid conversions (commented to avoid error)
# invalid_str = "abc"
# print(int(invalid_str))  # Will raise ValueError

# Use try-except to safely handle typecasting errors
s = "hello"
try:
    print(int(s))
except ValueError:
    print(f"Cannot convert '{s}' to int")

# Control statement example using a variable
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

if for_sale:
    print("This item is for sale.")
else:
    print("Not for sale.")
"""
Summary of this file:
Variables and how they store data
Integer, float, and boolean variable examples
If-else control statements for condition checking
Typecasting examples between different data types:
int, float, complex, str, repr, bool
list, tuple, set, frozenset, dict
bytes, bytearray, memoryview
chr, ord, ascii
bin, oct, hex, format
Converted a float to int using int()
"""
