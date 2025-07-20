
# File handling is used to perform CRUD operations: Create, Read, Update, and Delete.
# File modes:
# 'r'  : read (file must exist)
# 'w'  : write (overwrites existing file or creates new)
# 'a'  : append (adds content at the end of file without modifying existing content)
# 'x'  : exclusive creation (creates file, but error if it already exists)
# 'rb' : read binary
# 'wb' : write binary
# 'ab' : append binary

# Example 1: Create file using 'x' mode (will throw error if file exists)
# r = open(r"twxtfile.txt", 'x')
# r.write("Hello!")
# r.close()

# Example 2: Append content to a file (safe way to add content at the end)
q = open(r"twxtfile.txt", 'a')
q.write("\nHow are You")
q.close()

# Example 3: Write mode - this will remove existing content
w = open(r"twxtfile.txt", 'w')
w.write("Previous content removed \n")
w.close()

# Example 4: Writing to a file in a specific path using raw string (r"")
# This avoids treating \ as escape characters
qwe = open(r"C:\Users\win10\Desktop\h.txt", 'a')
qwe.write("See YOU Later Champion\n")
qwe.close()

"""
In this file, we covered:
- File creation and writing using open() with different modes ('x', 'w', 'a')
- File path specification using raw strings
- Understanding file modes and their purposes (read, write, append, exclusive create)
"""
