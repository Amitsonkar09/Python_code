# Understanding Decorators
# This file demonstrates how to create and use decorators in Python.

def decorator_function(original_function):
    """A simple decorator that adds functionality to the original function."""
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    """Function to display a message."""
    return "Display function executed!"

# Calling the decorated function
print(display())
