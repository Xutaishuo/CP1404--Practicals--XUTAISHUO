"""
CP1404/CP5632 Practical
Read scores.csv and display scores per subject with max, min and average.
"""


def main():
    """Read and display student scores from scores file."""
    with open("scores.csv") as scores_file:
        scores_data = scores_file.readlines()

    subjects = scores_data[0].strip().split(",")

    score_values = []
    for score_line in scores_data[1:]:
        if score_line.strip():
            score_strings = score_line.strip().split(",")
            score_numbers = [int(value) for value in score_strings]
            score_values.append(score_numbers)

    # 按科目整理分数：每个科目一列
    subject_scores = {}
    for i, subject in enumerate(subjects):
        subject_scores[subject] = [row[i] for row in score_values]

    # b/c: 打印每个科目的 10 个分数、最大值、最小值、平均值
    for subject in subjects:
        scores = subject_scores[subject]
        print(f"{subject} Scores:")
        for score in scores:
            print(score)
        print(f"Max: {max(scores)}")
        print(f"Min: {min(scores)}")
        print(f"Average: {sum(scores) / len(scores):.2f}")
        print()

    # d: 格式化表格
    print(f"{'Subject':<10} {'Scores':<40} {'Max':>4} {'Min':>4} {'Average':>8}")
    print("-" * 72)
    for subject in subjects:
        scores = subject_scores[subject]
        scores_text = " ".join(f"{score:3}" for score in scores)
        average = sum(scores) / len(scores)
        print(f"{subject:<10} {scores_text:<40} {max(scores):>4} {min(scores):>4} {average:>8.2f}")


if __name__ == "__main__":
    main()