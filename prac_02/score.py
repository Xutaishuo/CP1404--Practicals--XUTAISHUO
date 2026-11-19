"""
CP1404/CP5632 - Practical
Program to determine score status
Name:XU TAISHUO
JCU ID:JD177905
"""

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


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")
    if score == 100:
        print("You get a prize!")


if __name__ == "__main__":
    main()