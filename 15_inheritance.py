# Understanding Inheritance
# This file demonstrates how to use inheritance in Python.

class Animal:
    """Base class representing an animal."""
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    """Derived class representing a dog."""
    
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    """Derived class representing a cat."""
    
    def speak(self):
        return f"{self.name} says meow!"

# Creating objects of the derived classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

# Calling the speak method
print(my_dog.speak())
print(my_cat.speak())
