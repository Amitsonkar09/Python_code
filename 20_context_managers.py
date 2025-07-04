# Using Context Managers
# This file demonstrates how to use context managers in Python.

# Using with statement for file handling
with open("context_example.txt", "w") as file:
    file.write("This is an example of using context managers.")

# Reading the file using context manager
with open("context_example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Custom context manager
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")

# Using the custom context manager
with MyContextManager() as manager:
    print("Inside the context.")
