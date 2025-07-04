# Handling Exceptions
# This file demonstrates how to handle exceptions in Python.

try:
    # Trying to divide by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Using finally block
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This will always execute.")
