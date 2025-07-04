# Working with Lists
# This file demonstrates how to create and manipulate lists in Python.

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Adding an element
fruits.append("orange")
print("Updated Fruits:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing banana:", fruits)

# Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)
