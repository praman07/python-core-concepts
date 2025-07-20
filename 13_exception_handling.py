
# Example 1: Handling ZeroDivisionError
a = int(input("Enter a number:\t"))

try:
    print(10 / a)
except ZeroDivisionError:
    print("You can't divide by zero.")

# Example 2: Generic Exception with else and finally
a = int(input("Enter a number:\t"))

try:
    print(10 / a)
except Exception as err:
    print(f"Exception occurred: {err}")
else:
    print("This runs when no exception occurs.")
finally:
    print("I run no matter what.")

# Example 3: Using raise to create custom exceptions
age = int(input("Enter your age:\t"))
if age < 18 or age > 50:
    raise ValueError("You are not perfect for the event.")

print("This line will not run if an exception is raised above.")

# Example 4: Raise combined with try-except to handle the error
umar = int(input("Enter your age:\t"))

try:
    if umar < 18 or umar > 50:
        raise ValueError("You are not eligible.")
except Exception as we:
    print("Exception handled due to invalid age.")
    print("Club opens soon.")

"""
In this file, we covered:
- try block: where we place risky code that might cause an error
- except block: used to handle both specific and general exceptions
- else block: runs only if no exception occurs
- finally block: runs no matter what, whether there's an error or not
- raise statement: used to throw custom errors manually
- Built-in exceptions used: ZeroDivisionError, ValueError
"""
