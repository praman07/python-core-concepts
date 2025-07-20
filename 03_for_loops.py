# Python For Loop
# The 'for' loop is used to iterate over a sequence (like a list, string, or range of numbers)

# Print numbers from 1 to 20 using range(start, stop)
for i in range(1, 21):
    print(i)

# Print numbers from 0 to 50 using range(stop)
# If only one argument is provided, it is treated as the stop value, and start defaults to 0
for i in range(51):
    print(i)

# Print numbers from 10 to 1 using a reverse range
# range(start, stop, step) where step is negative for reverse order
for i in range(10, 0, -1):
    print(i)

# Print a multiplication table for a user input number using formatted strings
table_num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{table_num} * {i} = {table_num * i}")

# Print multiplication table using range step size
n = int(input("Enter a number: "))
for x in range(n, (n * 10) + 1, n):
    print(x)

# Loop through a string using indexing
word = "Helloworld"
print(f"Length of word: {len(word)}")
for i in range(len(word)):
    print(word[i])

# Loop through a string directly (without using index)
name = "miles"
for char in name:
    print(char)

# Print natural numbers up to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

# Reverse loop from n to 1
no = int(input("Enter number for reverse loop: "))
for i in range(no, 0, -1):
    print(i)

# Calculate the sum of numbers from 1 to (n + 9)
z = int(input("Enter number for sum: "))
total_sum = 0
for i in range(1, z + 10):
    total_sum += i
    print(total_sum)

# Calculate factorial of a number using for loop
f = int(input("Enter number to find factorial: "))
factorial = 1
for i in range(1, f + 1):
    factorial *= i
    print(factorial)

# Calculate sum of even and odd numbers up to n
num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

# Print factors of a number
number = int(input("Enter number to find factors: "))
print("Factors are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# Check if a number is perfect
# A perfect number is equal to the sum of its proper divisors
perfect = int(input("Enter a number to check if it's perfect: "))
factor_sum = 0
for i in range(1, perfect):
    if perfect % i == 0:
        factor_sum += i
print(f"Sum of factors: {factor_sum}")
if factor_sum == perfect:
    print("This is a perfect number.")
else:
    print("This is not a perfect number.")

# Check if a number is prime
# A prime number has exactly two factors: 1 and itself
prime_check = int(input("Enter number to check if it's prime: "))
factor_count = 0
for i in range(1, prime_check + 1):
    if prime_check % i == 0:
        factor_count += 1
print(f"Total factors: {factor_count}")
if factor_count == 2:
    print("This is a prime number.")
else:
    print("This is not a prime number.")
    
"""
Summary of this file:
Used for loops to print sequences of numbers using range
Printed multiplication tables using range and user input
Used for loop to iterate over strings (by index and by character)
Printed numbers in reverse using a decrementing loop
Calculated sum of numbers, even and odd sums
Calculated factorial of a number using loop
Found and printed factors of a number
Checked whether a number is perfect
Checked whether a number is prime by counting its factors
"""
