"""
CP1404/CP5632 Practical
Programming Language class
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of the language
        typing: string, 'Static' or 'Dynamic'
        reflection: boolean, whether it supports reflection
        year: integer, year it first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"