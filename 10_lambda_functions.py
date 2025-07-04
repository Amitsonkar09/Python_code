# Introduction to Lambda Functions
# This file demonstrates how to use lambda functions in Python.

# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

# Calling the functions
print("Regular function result:", add(5, 3))
print("Lambda function result:", add_lambda(5, 3))

# Using lambda with filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
