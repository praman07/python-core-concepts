# Python Nested Loops
# A nested loop means a loop inside another loop.
# The inner loop runs completely for every single iteration of the outer loop.

# Print pattern of stars in a square
rows = int(input("Enter number of rows for square pattern: "))
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

# Right-angled triangle star pattern
height = int(input("Enter height for right-angled triangle pattern: "))
for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Print multiplication tables from 1 to 5
for table in range(1, 6):
    print(f"\nMultiplication table of {table}")
    for i in range(1, 11):
        print(f"{table} * {i} = {table * i}")

# Print all pairs (i, j) where i from 1-3 and j from 1-2
for i in range(1, 4):
    for j in range(1, 3):
        print(f"Pair: ({i}, {j})")

# Nested loop with condition (print only even products in table)
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        if product % 2 == 0:
            print(f"{i} * {j} = {product}")
    print()

# Nested loop for reverse triangle pattern
n = int(input("Enter rows for reverse triangle: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Print a grid of numbers
rows = 3
cols = 4
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(j, end=" ")
    print()

"""
Summary of this file:
Used nested for loops to build square, triangle, and reverse triangle patterns
Printed multiplication tables using loops inside loops
Demonstrated pairing using nested iterations
Added conditions inside inner loops for selective printing
Created a numeric grid using nested loops
"""
