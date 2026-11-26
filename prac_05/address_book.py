"""
CP1404/CP5632 Practical
Address Book program using a dictionary.
"""

MENU = """(A)dd new friend
(C)hange address
(P)rint address
(Q)uit"""


def main():
    """Run the friend address book program."""
    name_to_address = {}
    print("Welcome to the Friend Address Book!")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            add_friend(name_to_address)
        elif choice == "C":
            change_address(name_to_address)
        elif choice == "P":
            print_address(name_to_address)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


def add_friend(name_to_address):
    """Add a new name and address to the dictionary."""
    name = input("Enter name: ").strip()
    if name in name_to_address:
        print("This name already exists! Please use the 'Change' option.")
    else:
        address = input("Enter address: ").strip()
        name_to_address[name] = address
        print(f"Added {name}.")


def change_address(name_to_address):
    """Change the address for an existing entry."""
    name = input("Enter name to update: ").strip()
    if name in name_to_address:
        new_address = input("Enter new address: ").strip()
        name_to_address[name] = new_address
        print("Address updated.")
    else:
        print("Name not found.")


def print_address(name_to_address):
    """Print the address of a chosen name."""
    name = input("Enter name to look up: ").strip()
    if name in name_to_address:
        print(f"{name}'s address is: {name_to_address[name]}")
    else:
        print("Name not found.")


if __name__ == "__main__":
    main()