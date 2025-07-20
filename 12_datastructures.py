
# LISTS
# Lists are ordered, mutable collections that allow duplicate elements.
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")
fruits.append("orange")  # Adds at the end
fruits.insert(1, "grape")  # Adds at specific index
fruits.remove("banana")  # Removes by value
print(f"Updated list: {fruits}")
print(f"Access index 2: {fruits[2]}")
print(f"List slicing: {fruits[1:3]}")
print(f"Length of list: {len(fruits)}")
fruits.sort()
print(f"Sorted list: {fruits}")
fruits.reverse()
print(f"Reversed list: {fruits}")
print("Looping through list:")
for item in fruits:
    print(item)

# Common list methods
print(f"Pop last item: {fruits.pop()}")  # Removes last item and returns it
fruits.extend(["kiwi", "mango"])  # Adds multiple items
print(f"Extended list: {fruits}")
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Index of 'grape': {fruits.index('grape')}")
copied_list = fruits.copy()  # Creates a shallow copy
fruits.clear()  # Empties the list
print(f"Cleared original list: {fruits}")
print(f"Copied list remains: {copied_list}")

# TUPLES
# Tuples are ordered, immutable collections. They allow duplicates.
dimensions = (10, 20, 30)
print(f"Tuple: {dimensions}")
print(f"First element: {dimensions[0]}")
print(f"Slicing tuple: {dimensions[1:]}")
print(f"Length of tuple: {len(dimensions)}")

# SETS
# Sets are unordered, mutable (but elements must be immutable), and do not allow duplicates.
unique_numbers = {1, 2, 3, 4, 5, 3, 2}
print(f"Set with duplicates removed: {unique_numbers}")
unique_numbers.add(6)
unique_numbers.discard(2)
print(f"Updated set: {unique_numbers}")
print(f"Is 3 in the set? {'Yes' if 3 in unique_numbers else 'No'}")
print("Looping through set:")
for num in unique_numbers:
    print(num)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric difference: {a ^ b}")

# DICTIONARIES
# Dictionaries are unordered collections of key-value pairs.
student = {
    "name": "Alice",
    "age": 21,
    "course": "BCA"
}
print(f"Student dictionary: {student}")
print(f"Access by key: {student['name']}")
student["age"] = 22  # Update value
student["grade"] = "A"  # Add new key-value pair
print(f"Updated dictionary: {student}")
del student["course"]  # Delete a key
print(f"Dictionary after deletion: {student}")

# Looping through dictionary
for key, value in student.items():
    print(f"{key} : {value}")

# Get method and keys/values
print(f"Get age: {student.get('age')}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# SHALLOW COPY
# A shallow copy creates a new outer list, but inner objects are still shared (same references)
original = [[1, 2], [3, 4]]
shallow = original.copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow}")

original[0][0] = 99
print(f"After modifying original[0][0] to 99")
print(f"Original: {original}")
print(f"Shallow copy: {shallow}")  # Change appears here too

original.append([5, 6])
print(f"After appending to original")
print(f"Original: {original}")
print(f"Shallow copy: {shallow}")  # No change here (outer list is different)

# DEEP COPY
# Deep copy creates a completely independent copy of both outer and inner elements.
import copy
deep = copy.deepcopy(original)
original[0][1] = 100
print(f"After modifying original[0][1] to 100")
print(f"Original: {original}")
print(f"Deep copy: {deep}")  # No change here — fully independent

"""
In this file, we covered:
- Lists: definition, methods (append, insert, pop, extend, clear, count, index, copy), slicing, looping, sorting
- Tuples: immutability, indexing, slicing
- Sets: uniqueness, operations (add, discard, union, etc.)
- Dictionaries: key-value operations, updating, deleting, looping
- Shallow copy: .copy() creates a new outer list, but inner elements are still shared
- Deep copy: deepcopy() creates a completely independent nested copy
"""
