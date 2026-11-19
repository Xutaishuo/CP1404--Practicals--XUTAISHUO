"""
CP1404/CP5632 - Practical
Gopher Population Simulator
"""

import random

STARTING_POPULATION = 1000
YEARS = 10
MIN_BIRTH_RATE = 0.10
MAX_BIRTH_RATE = 0.20
MIN_DEATH_RATE = 0.05
MAX_DEATH_RATE = 0.25


def main():
    """Simulate the gopher population over ten years."""
    print("Welcome to the Gopher Population Simulator!")
    population = STARTING_POPULATION
    print(f"Starting population: {population}")

    for year in range(1, YEARS + 1):
        print(f"Year {year}")
        print()

        birth_rate = random.uniform(MIN_BIRTH_RATE, MAX_BIRTH_RATE)
        death_rate = random.uniform(MIN_DEATH_RATE, MAX_DEATH_RATE)

        born = int(population * birth_rate)
        died = int(population * death_rate)

        population = population + born - died

        print(f"{born} gophers were born. {died} died.")
        print(f"Population: {population}")


if __name__ == "__main__":
    main()