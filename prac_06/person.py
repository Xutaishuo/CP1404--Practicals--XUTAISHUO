"""
CP1404/CP5632 Practical
Person class
"""


class Person:
    """Represent a person with a first name, last name, and age."""

    def __init__(self, first_name="", last_name="", age=0):
        """Initialise a Person instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Return a string representation of the Person."""
        return f"{self.first_name} {self.last_name}, {self.age}"