"""
CP1404/CP5632 - Practical
File size: count the number of lines in a file.
"""


def main():
    """Ask for filenames until the user enters an empty string."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            line_count = count_lines(filename)
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        else:
            print(f"{filename} has {line_count} lines.")
        filename = input("Enter filename: ")


def count_lines(filename):
    """Return the number of lines in the given file."""
    with open(filename, "r") as in_file:
        line_count = 0
        for _ in in_file:
            line_count += 1
    return line_count


if __name__ == "__main__":
    main()