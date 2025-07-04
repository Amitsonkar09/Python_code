# If, Elif, and Else Statements
# This file demonstrates how to use conditional statements in Python.

# Defining a variable
age = 18

# Using if, elif, and else
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")

# Checking multiple conditions
if age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior citizen.")
else:
    print("You are a minor.")
