# Introduction to Dictionaries
# This file demonstrates how to create and use dictionaries in Python.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person Dictionary:", person)

# Accessing values
print("Name:", person["name"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("Updated Person Dictionary:", person)

# Removing a key-value pair
del person["age"]
print("After removing age:", person)

# Looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
