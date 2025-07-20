
# Topic: String Operations and Manipulations

# Strings are ordered sequences of characters and are immutable in Python.
# They can be created using single, double, or triple quotes.

# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is a multi-line
string.'''
print(s1, s2)
print(s3)

# Length of a string using len()
print("Length of s1:", len(s1))

# String concatenation (joining strings)
first = "Hello"
second = "World"
combined = first + " " + second
print("Concatenated string:", combined)

# String repetition using *
greet = "Hi "
print("Repetition:", greet * 3)

# String indexing (positive and negative)
word = "Python"
print("First character:", word[0])
print("Last character:", word[-1])

# String slicing [start:stop] (stop is not included)
print("Characters from index 1 to 3:", word[1:4])
print("From beginning to index 3:", word[:4])
print("From index 2 to end:", word[2:])
print("Full string using slicing:", word[:])

# Reversing a string using slicing
string1 = input("Enter a string to reverse (slicing method): ")
reversed_string1 = string1[::-1]
print("Reversed string:", reversed_string1)

# Reversing a string using a loop
string2 = input("Enter a string to reverse (loop method): ")
reversed_str = ""
for i in range(len(string2) - 1, -1, -1):
    reversed_str += string2[i]
print("Reversed string:", reversed_str)

# Check if a string is a palindrome
pal = input("Enter a string to check for palindrome: ")
rev = pal[::-1]
if pal == rev:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")

# Looping through a string using index
word = "Helloworld"
for i in range(len(word)):
    print(word[i])

# Looping through a string without index
name = "miles"
for char in name:
    print(char)

# Counting alphabets, digits, and special characters
user_str = input("Enter any text: ")
digit_count = 0
alpha_count = 0
special_count = 0
for char in user_str:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1
print("Alphabets:", alpha_count)
print("Digits:", digit_count)
print("Special characters:", special_count)

# Common string methods

text = "   Hello, Python! 123   "

# Strip removes spaces from both ends
print("Original:", text)
print("Stripped:", text.strip())

# Lower and upper case
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())

# Replace characters
print("Replace 'H' with 'J':", text.replace("H", "J"))

# Find and index
print("Find position of 'Python':", text.find("Python"))  # returns -1 if not found
# index() gives error if not found
print("Index of ',' character:", text.index(","))

# Count occurrences of a character
print("Count of 'l':", text.count("l"))

# Startswith and endswith
print("Starts with '   H':", text.startswith("   H"))
print("Ends with '123   ':", text.endswith("123   "))

# Split a string into a list
csv = "apple,banana,mango"
fruits = csv.split(",")
print("Split list:", fruits)

# Join a list into a string
joined = " | ".join(fruits)
print("Joined string:", joined)

# Escape characters
print("New line:\nSecond line")
print("Tab\tIndented text")
print("Quotes inside: \"double quotes\" and \'single quotes\'")

# String formatting methods

name = "Alice"
age = 25

# 1. f-string (Recommended)
print(f"{name} is {age} years old")

# 2. format() method
print("{} is {} years old".format(name, age))

# 3. % formatting (older)
print("%s is %d years old" % (name, age))

"""
Summary of this file:
String creation using single, double, and triple quotes
String concatenation and repetition
Indexing and slicing strings
Reversing strings using slicing and loops
Checking for palindromes
Looping through strings with and without index
Counting alphabets, digits, and special characters
Using string methods: strip, lower, upper, replace, find, index, count, startswith, endswith
Splitting and joining strings
Escape characters like newline, tab, and quotes
String formatting using f-strings, format(), and % formatting
"""
