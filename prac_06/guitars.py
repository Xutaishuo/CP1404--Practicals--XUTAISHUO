"""
CP1404/CP5632 Practical
Client code for the Guitar class.
"""

from prac_06.guitar import Guitar


def main():
    """Read guitars from user and display them."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        # 使用三元运算符判断是否为 vintage
        vintage_string = " (vintage)" if guitar.is_vintage() else ""

        # 按照题目要求的格式对齐输出
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()