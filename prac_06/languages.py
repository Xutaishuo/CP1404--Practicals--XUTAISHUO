"""
CP1404/CP5632 Practical
Client code for ProgrammingLanguage class
"""

from programming_language import ProgrammingLanguage


def main():
    """Demo test code to show how to use the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # 1. Print python object to test __str__
    print(python)

    # 2. Create a list containing the three objects
    languages = [python, ruby, visual_basic]

    # 3. Loop and print the names of all dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()