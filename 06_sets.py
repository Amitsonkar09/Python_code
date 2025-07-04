# Working with Sets
# This file demonstrates how to create and manipulate sets in Python.

# Creating a set
fruits_set = {"apple", "banana", "cherry"}
print("Fruits Set:", fruits_set)

# Adding an element
fruits_set.add("orange")
print("Updated Fruits Set:", fruits_set)

# Removing an element
fruits_set.remove("banana")
print("After removing banana:", fruits_set)

# Checking membership
print("Is apple in the set?", "apple" in fruits_set)

# Looping through a set
for fruit in fruits_set:
    print("Fruit:", fruit)
