# Inheritance in Python

This project explores the concept of inheritance in Python, which allows one class (the subclass) to inherit attributes and methods from another class (the superclass).

## Overview

Inheritance enables code reusability and establishes a relationship between classes. It allows subclasses to override or extend the functionalities of their parent classes.

## Key Concepts

### 1. Superclass (Base Class)
The class whose properties and methods are inherited by another class.

### 2. Subclass (Derived Class)
The class that inherits from the superclass. It can have its own methods and attributes in addition to those inherited.

### 3. Method Overriding
A subclass can provide a specific implementation of a method that is already defined in its superclass.

### 4. Using `super()`
The `super()` function is used to call a method from the superclass within a subclass.

## Example

Here is a simple example demonstrating inheritance:

```python
#!/usr/bin/python3
"""This module demonstrates inheritance in Python."""

class Animal:
    """A simple representation of an animal."""
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    """A Dog class that inherits from Animal."""
    
    def speak(self):
        return "Bark"

# Creating an instance of Dog
my_dog = Dog()
print(my_dog.speak())  # Output: Bark