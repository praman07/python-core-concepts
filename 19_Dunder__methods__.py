#Dunder meeans __ double underscores 
# DUNDER (Double Underscore) METHODS
# These are special methods in Python that begin and end with double underscores.
# They're used to define how objects behave with built-in operations.

# __init__ : Constructor, used to initialize object attributes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # __str__ : Defines how the object is printed with print()
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ : Returns the length when len(obj) is called
    def __len__(self):
        return len(self.title)

    # __eq__ : Compares two objects using ==
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # __add__ : Defines behavior for + operator
    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.author + " & " + other.author)


book1 = Book("Python Basics", "Alice")
book2 = Book("Advanced Python", "Bob")
book3 = Book("Python Basics", "Alice")

print(book1)                      # Uses __str__
print(len(book1))                # Uses __len__
print(book1 == book3)            # Uses __eq__
combined = book1 + book2         # Uses __add__
print(combined)

# __repr__ : Official string representation of the object, useful for debugging
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name='{self.name}')"


s = Student("Praman")
print(repr(s))

# __getitem__, __setitem__, __delitem__ : Indexing behavior for custom objects
class CustomList:
    def __init__(self, elements):
        self.data = elements

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]


clist = CustomList([1, 2, 3, 4])
print(clist[1])        # Uses __getitem__
clist[1] = 99          # Uses __setitem__
print(clist[1])
del clist[1]           # Uses __delitem__
print(clist.data)

# __call__ : Makes an object callable like a function
class Greet:
    def __call__(self, name):
        print(f"Hello, {name}!")


g = Greet()
g("Praman")  # Acts like calling a function

"""
In this file, we covered:
- __init__, __str__, __repr__
- __len__, __eq__, __add__
- __getitem__, __setitem__, __delitem__
- __call__
All of these are examples of dunder (magic) methods.
"""
