"""
CP1404/CP5632 Practical
Wimbledon Champions program
Estimate: 20 minutes
Actual:   15 minutes
"""

import csv


def main():
    """Read Wimbledon data and display champions and their countries."""
    filename = "wimbledon.csv"

    # 1. 读取数据为 list of lists
    data = read_data(filename)

    # 2. 处理数据得到字典 (冠军 -> 获胜次数) 和集合 (国家)
    champion_to_count = process_champions(data)
    countries = process_countries(data)

    # 3. 打印结果
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print()
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def read_data(filename):
    """Read the CSV file and return a list of lists, skipping the header."""
    data = []
    # 使用 utf-8-sig 处理带有 BOM 的 UTF-8 文件
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # 跳过第一行表头
        for row in reader:
            data.append(row)
    return data


def process_champions(data):
    """Create a dictionary of champion names and their win counts."""
    champion_to_count = {}
    for row in data:
        # 冠军名字在第 2 列（索引为 2）
        champion = row[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def process_countries(data):
    """Create a set of unique countries that have won Wimbledon."""
    countries = set()
    for row in data:
        # 冠军所属国家在第 1 列（索引为 1）
        country = row[1]
        countries.add(country)
    return countries


if __name__ == "__main__":
    main()