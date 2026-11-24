"""
CP1404/CP5632 Practical
Test code for the Guitar class.
"""

from prac_06.guitar import Guitar


def main():
    """Test the Guitar class methods."""
    # Create an instance of Guitar (using dynamic year to adapt to current time)
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    # Test get_age()
    # Note: The expected age will change as the years go by, so we calculate it dynamically for the test
    import datetime
    current_year = datetime.datetime.now().year

    expected_age1 = current_year - 1922
    expected_age2 = current_year - 2013

    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


if __name__ == "__main__":
    main()