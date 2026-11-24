"""
CP1404/CP5632 Practical
Client code for Person class - read and display a table of people.
"""

from prac_06.person import Person  # 如果在同一文件夹，直接用 from person import Person


def main():
    """Read people from user and display them sorted by age."""
    print("Persons")
    people = []

    first_name = input("First name: ")
    while first_name != "":
        last_name = input("Last name: ")
        age = int(input("Age: "))

        people.append(Person(first_name, last_name, age))

        first_name = input("First name: ")

    # 按年龄从小到大排序
    people.sort(key=lambda p: p.age)

    # 打印格式化的表格
    print("\nPerson Table:")
    if not people:
        print("No people entered.")
        return

    # 动态计算最长名字的宽度以便对齐
    max_first_len = max(len(p.first_name) for p in people)
    max_last_len = max(len(p.last_name) for p in people)

    for p in people:
        print(f"{p.first_name:<{max_first_len}} | {p.last_name:<{max_last_len}} | {p.age}")


if __name__ == "__main__":
    main()