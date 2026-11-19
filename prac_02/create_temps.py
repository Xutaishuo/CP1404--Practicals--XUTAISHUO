"""
CP1404/CP5632 - Practical
Create a text file with random Fahrenheit temperatures.
"""

import random


def main():
    """Create temps_input.txt with 15 random floats between -200 and 200."""
    with open("temps_input.txt", "w") as out_file:
        for _ in range(15):
            temperature = random.uniform(-200, 200)
            out_file.write(f"{temperature}\n")
    print("Created temps_input.txt with 15 random Fahrenheit values.")


if __name__ == "__main__":
    main()