# Introduction to Classes and Objects
# This file demonstrates how to create and use classes in Python.

class Dog:
    """A simple class representing a dog."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods
print("Dog's Name:", my_dog.name)
print("Dog's Age:", my_dog.age)
print(my_dog.bark())
