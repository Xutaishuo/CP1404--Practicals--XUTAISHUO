"""
CP1404/CP5632 Practical
Word Occurrences program
Estimate: 15 minutes
Actual:   10 minutes
"""


def main():
    """Count and display the occurrences of words in a string."""
    text = input("Text: ")
    words = text.split()

    # 1. Count occurrences using a dictionary
    word_counts = {}
    for word in words:
        # .get(word, 0) returns 0 if the word is not in the dictionary yet
        word_counts[word] = word_counts.get(word, 0) + 1

    # 2. Find the longest word to determine the width for alignment
    max_length = max(len(word) for word in word_counts)

    # 3. Sort the dictionary items alphabetically by the word (the key)
    sorted_word_counts = sorted(word_counts.items())

    # 4. Print with dynamic width alignment
    for word, count in sorted_word_counts:
        print(f"{word:{max_length}} : {count}")


if __name__ == "__main__":
    main()