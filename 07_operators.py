
# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Assignment Operators
x = 5
print("\nAssignment Operators:")
x += 2
print(f"x += 2 : {x}")
x -= 1
print(f"x -= 1 : {x}")
x *= 3
print(f"x *= 3 : {x}")
x /= 2
print(f"x /= 2 : {x}")
x %= 3
print(f"x %= 3 : {x}")
x **= 2
print(f"x **= 2 : {x}")
x //= 2
print(f"x //= 2 : {x}")

# Comparison Operators
m = 10
n = 20
print("\nComparison Operators:")
print(f"{m} == {n} : {m == n}")
print(f"{m} != {n} : {m != n}")
print(f"{m} > {n} : {m > n}")
print(f"{m} < {n} : {m < n}")
print(f"{m} >= {n} : {m >= n}")
print(f"{m} <= {n} : {m <= n}")

# Logical Operators
a = True
b = False
print("\nLogical Operators:")
print(f"a and b : {a and b}")
print(f"a or b : {a or b}")
print(f"not a : {not a}")

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("\nIdentity Operators:")
print(f"x is y : {x is y}")
print(f"x is z : {x is z}")
print(f"x is not z : {x is not z}")

# Membership Operators
nums = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print(f"3 in nums : {3 in nums}")
print(f"6 not in nums : {6 not in nums}")

# Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print("\nBitwise Operators:")
print(f"a & b (AND)     : {a & b}")   # 0000 0100 → 4
print(f"a | b (OR)      : {a | b}")   # 0000 1110 → 14
print(f"a ^ b (XOR)     : {a ^ b}")   # 0000 1010 → 6
print(f"~a (NOT)        : {~a}")      # Inverts bits → -(a+1) = -11
print(f"a << 2 (Left Shift)  : {a << 2}")  # 101000 → 40
print(f"a >> 2 (Right Shift) : {a >> 2}")  # 0010 → 2

"""
In this file, we covered:
- Arithmetic operators: +, -, *, /, %, //, **
- Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
- Comparison operators: ==, !=, >, <, >=, <=
- Logical operators: and, or, not
- Identity operators: is, is not
- Membership operators: in, not in
- Bitwise operators: &, |, ^, ~, <<, >>
"""
