"""
CP1404/CP5632 Practical
Car Driving Simulator program
"""

from prac_06.car import Car  # 如果在同一文件夹，直接用 from car import Car


def main():
    """Run the car driving simulator."""
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    # 初始化汽车，默认 100 燃料
    car = Car(car_name, 100)

    print(car)  # 调用 __str__
    print_menu()
    choice = input("Enter your choice: ").lower()

    while choice != "q":
        if choice == "d":
            handle_drive(car)
        elif choice == "r":
            handle_refuel(car)
        else:
            print("Invalid choice")

        print()
        print(car)
        print_menu()
        choice = input("Enter your choice: ").lower()

    print(f"\nGood bye {car.name}'s driver.")


def print_menu():
    """Print the menu options."""
    print("Menu:")
    print("d) drive")
    print("r) refuel")
    print("q) quit")


def handle_drive(car):
    """Handle the drive option, including input validation and outcomes."""
    distance = int(input("How many km do you wish to drive? "))
    while distance < 0:
        print("Distance must be >= 0")
        distance = int(input("How many km do you wish to drive? "))

    actual_distance = car.drive(distance)

    if actual_distance < distance:
        print(f"The car drove {actual_distance}km and ran out of fuel.")
    else:
        print(f"The car drove {actual_distance}km.")


def handle_refuel(car):
    """Handle the refuel option, including input validation."""
    fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    while fuel_amount < 0:
        print("Fuel amount must be >= 0")
        fuel_amount = int(input("How many units of fuel do you want to add to the car? "))

    car.add_fuel(fuel_amount)
    print(f"Added {fuel_amount} units of fuel.")


if __name__ == "__main__":
    main()