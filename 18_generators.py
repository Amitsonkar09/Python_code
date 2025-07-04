# Introduction to Generators
# This file demonstrates how to create and use generators in Python.

def count_up_to(max):
    """Generator function to count up to a maximum number."""
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print("Count:", number)

# Generator expression
squared_gen = (x**2 for x in range(5))
print("Squared numbers from generator expression:")
for square in squared_gen:
    print(square)
