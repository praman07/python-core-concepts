# Python If-Else Statements
# Used for decision-making in programs. Executes code blocks based on conditions.

# Simple if condition
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")

# If-else condition
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# If-elif-else ladder
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested if statement
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

# Checking if a number is positive, negative, or zero
x = int(input("Enter a number: "))
if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")

# Use of logical operators in conditions
username = input("Enter username: ")
password = input("Enter password: ")
if username == "user" and password == "pass":
    print("Login successful")
else:
    print("Login failed")

# Use of membership operator
city = input("Enter city name: ")
if city in ["Delhi", "Mumbai", "Chennai"]:
    print("Metro city")
else:
    print("Non-metro city")

# Use of identity operator
x = None
y = None
if x is y:
    print("x and y are the same object")

"""
Summary of this file:
Used if, if-else, and if-elif-else statements for conditional logic
Handled nested if conditions with login example
Demonstrated use of logical operators (and, or)
Checked values using membership and identity operators
Covered common scenarios: voting, grades, login, number properties
"""
