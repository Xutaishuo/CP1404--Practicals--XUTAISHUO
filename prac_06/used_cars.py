"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # 修改：原来的 Car(180) 加上名字
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")

    # 1. 创建一个名为 limo 的新车，初始燃料 100
    limo = Car("Limo", 100)

    # 2. 给这辆车加 20 单位燃料
    limo.add_fuel(20)

    # 3. 打印这辆车目前的燃料量
    print(f"Limo has fuel: {limo.fuel}")

    # 4. 尝试驾驶 115 km
    limo.drive(115)
    # (注意：车里有 120 燃料，行驶 115 km 后，剩余 5 燃料)

    # 打印车辆对象以测试 __str__ 方法
    print(my_car)
    print(limo)


main()