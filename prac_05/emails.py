"""
CP1404/CP5632 Practical
Emails and Names dictionary program
Estimate: 20 minutes
Actual:   15 minutes
"""


def main():
    """Store users' emails and names in a dictionary, then print them."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)

        # Ask for confirmation. Default is Yes (Y) if the user just presses Enter.
        is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_correct != "" and is_correct != "y":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from an email address, e.g., lindsay.ward@jcu.edu.au -> Lindsay Ward."""
    # Get the part before the @ symbol
    prefix = email.split('@')[0]
    # Split by dots to separate first and last name
    parts = prefix.split('.')
    # Join with a space and convert to title case
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()