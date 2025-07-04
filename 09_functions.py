# Defining and Calling Functions
# This file demonstrates how to define and call functions in Python.

# Defining a function
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))
print(greet("Bob"))

# Function with default parameter
def greet_with_default(name="Guest"):
    """Function to greet a person with a default name."""
    return f"Hello, {name}!"

# Calling the function with default parameter
print(greet_with_default())
