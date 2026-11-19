"""
CP1404/CP5632 - Practical
Convert Fahrenheit temperatures from a file to Celsius.
"""


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


def main():
    """Read Fahrenheit values and write Celsius values to a file."""
    with open("temps_input.txt", "r") as in_file, open("temps_output.txt", "w") as out_file:
        for line in in_file:
            line = line.strip()
            if line:
                fahrenheit = float(line)
                celsius = fahrenheit_to_celsius(fahrenheit)
                out_file.write(f"{celsius}\n")
    print("Converted temperatures written to temps_output.txt")


if __name__ == "__main__":
    main()