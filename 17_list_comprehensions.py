# Using List Comprehensions
# This file demonstrates how to use list comprehensions in Python.

# Regular list creation
squares = []
for x in range(10):
    squares.append(x**2)

print("Squares using loop:", squares)

# List comprehension
squares_comp = [x**2 for x in range(10)]
print("Squares using list comprehension:", squares_comp)

# Filtering with list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)
