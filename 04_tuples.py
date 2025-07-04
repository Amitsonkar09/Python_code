# Understanding Tuples
# This file demonstrates how to create and use tuples in Python.

# Creating a tuple
colors = ("red", "green", "blue")
print("Colors:", colors)

# Accessing elements
print("First color:", colors[0])

# Tuples are immutable, so we cannot change them
# colors[0] = "yellow"  # This will raise an error

# Looping through a tuple
for color in colors:
    print("Color:", color)
