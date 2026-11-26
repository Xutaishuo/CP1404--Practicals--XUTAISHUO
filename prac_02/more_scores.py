"""
CP1404/CP5632 - Practical
More scores: generate random scores and write results to a file
NAME:XU TAISHUO
JCU ID:JD177905
"""

import random


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
    number_of_scores = int(input("How many random scores? "))
    with open("results.txt", "w") as out_file:
        for _ in range(number_of_scores):
            score = random.randint(0, 100)
            result = determine_result(score)
            print(f"Random: {score} = {result}")
            out_file.write(f"{score} is {result}\n")


if __name__ == "__main__":
    main()