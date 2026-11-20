"""
CP1404/CP5632 - Practical
File reading and writing examples
"""

# 1. Ask for a name, then write it to name.txt using open and close.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()


# 2. Read the name from name.txt and print "Hi ...!" using open and close.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# 3. Read only the first two numbers from numbers.txt and print their sum.
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)


# 4. Print the total of all numbers in numbers.txt.
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
print(total)