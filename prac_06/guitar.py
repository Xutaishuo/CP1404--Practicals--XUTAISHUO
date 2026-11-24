"""
CP1404/CP5632 Practical
Guitar class
"""

import datetime


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar
        year: integer, year it was made
        cost: float, how much it costs
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() >= 50