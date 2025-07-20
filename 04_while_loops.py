# Python While Loops
# A while loop repeats a block of code as long as a condition is true.

# Print numbers from 1 to 10 using while loop
count = 1
while count <= 10:
    print(count)
    count += 1

# Countdown from 10 to 1
x = 10
while x >= 1:
    print(x)
    x -= 1

# Print even numbers from 2 to 20
num = 2
while num <= 20:
    print(num)
    num += 2

# Print multiplication table of a number using while loop
number = int(input("Enter a number to print its table: "))
i = 1
while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i += 1

# Reverse a string using while loop
original = input("Enter a string to reverse: ")
reversed_str = ""
i = len(original) - 1
while i >= 0:
    reversed_str += original[i]
    i -= 1
print(f"Reversed string: {reversed_str}")

# Calculate factorial of a number using while loop
n = int(input("Enter number to find factorial: "))
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"Factorial is: {factorial}")

# Sum of digits of a number using while loop
number = int(input("Enter a number to find sum of digits: "))
sum_digits = 0
while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10
print(f"Sum of digits is: {sum_digits}")

# Count the number of digits in a number
num = int(input("Enter a number to count digits: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"Number of digits: {count}")

# Input validation using while loop (until user enters a positive number)
user_input = int(input("Enter a positive number: "))
while user_input <= 0:
    user_input = int(input("Please enter a positive number: "))
print(f"You entered: {user_input}")

# Find whether a number is prime using while loop
num = int(input("Enter a number to check if it's prime: "))
i = 2
is_prime = True
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if num > 1 and is_prime:
    print("This is a prime number.")
else:
    print("This is not a prime number.")

"""
Summary of this file:
Used while loop to print counting and reverse counting
Generated multiplication tables using while loops
Reversed strings using index-based while iteration
Calculated factorial of a number using a while loop
Computed sum of digits and counted digits using while logic
Validated user input using a conditional while loop
Checked whether a number is prime using while loop conditions
"""
