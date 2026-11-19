"""
CP1404/CP5632 - Practical
Score menu program
NAME:XU TAISHUO
JCU ID:JD177905
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score menu program."""
    print("Welcome to the score menu program.")
    score = get_valid_score()

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    """Get a score between 0 and 100 inclusive."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """Determine the result for a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print stars equal to the score."""
    print("*" * int(score))


if __name__ == "__main__":
    main()