"""
CP1404/CP5632 Practical
Electricity bill estimator 2.0 using a dictionary for tariffs.
"""

# 电价字典 (增加了 3 个虚构的电价：42, 55, 67)
TARIFFS = {
    11: 0.244618,
    31: 0.136928,
    42: 0.198500,
    55: 0.310200,
    67: 0.155000
}


def main():
    """Calculate and display an estimated electricity bill."""
    print("Electricity bill estimator 2.0")

    # 获取有效的电价代码
    tariff = get_valid_tariff()

    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    # 从字典中取出对应的费率并计算总价
    cost_per_kwh = TARIFFS[tariff]
    estimated_bill = cost_per_kwh * daily_use * billing_days

    print(f"Estimated bill: ${estimated_bill:.2f}")


def get_valid_tariff():
    """Get a valid tariff from the user based on dictionary keys."""
    # 动态生成提示语：把所有的键提取出来，转成字符串并用逗号连接
    # 比如 TARIFFS.keys() 是 dict_keys([11, 31, 42, 55, 67])
    # 下面这行代码会生成 "11, 31, 42, 55, 67"
    valid_tariffs_string = ", ".join(str(t) for t in TARIFFS.keys())

    prompt = f"Which tariff? {valid_tariffs_string}: "
    tariff = int(input(prompt))

    while tariff not in TARIFFS:
        print("Invalid tariff!")
        tariff = int(input(prompt))

    return tariff


if __name__ == "__main__":
    main()