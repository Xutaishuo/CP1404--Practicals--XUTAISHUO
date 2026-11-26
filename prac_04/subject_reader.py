"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_subject_data(FILENAME)
    display_subject_details(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file and return a list of [subject, lecturer, students] lists."""
    subject_data = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            if line:
                parts = line.split(',')
                subject_data.append([parts[0], parts[1], int(parts[2])])
    return subject_data


def display_subject_details(subject_data):
    """Display each subject's details."""
    for subject, lecturer, students in subject_data:
        print(f"{subject} is taught by {lecturer:12} and has {students:3} students")


if __name__ == "__main__":
    main()