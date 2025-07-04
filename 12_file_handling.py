# Reading and Writing Files
# This file demonstrates how to read from and write to files in Python.

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
