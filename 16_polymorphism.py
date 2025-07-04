# Introduction to Polymorphism
# This file demonstrates how to use polymorphism in Python.

class Bird:
    """Base class representing a bird."""
    
    def fly(self):
        return "Flies in the sky"

class Sparrow(Bird):
    """Derived class representing a sparrow."""
    
    def fly(self):
        return "Sparrow flies quickly"

class Ostrich(Bird):
    """Derived class representing an ostrich."""
    
    def fly(self):
        return "Ostrich cannot fly"

# Function to demonstrate polymorphism
def bird_flight(bird):
    print(bird.fly())

# Creating objects of the derived classes
sparrow = Sparrow()
ostrich = Ostrich()

# Calling the function with different objects
bird_flight(sparrow)
bird_flight(ostrich)
