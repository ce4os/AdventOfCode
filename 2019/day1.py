# --- Day 1: The Tyranny of the Rocket Equation --

from math import floor
from utils import get_puzzle_input_as_list


def calculate_total_fuel_needed(module_masses: list[int]) -> int:
    """Takes a list of ints, divides every int by 3, floors it, subtracts 2 and then calculates the sum of all"""
    return sum([(floor(module_mass/3) - 2) for module_mass in module_masses])


def calculate_fuel(mass: int) -> int:
    """calculates the fuel needed for a given mass, including the recursive calculation for the fuel needed for the fuel itself."""
    fuel = floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)


def calculate_total_fuel_needed2(module_masses: list[int]) -> int:
    """Same as calculate_total_fuel_needed but fuel needed also treated as the mass of the module"""
    return sum([calculate_fuel(module_mass) for module_mass in module_masses])
    

def main():
    # Init
    module_masses = [int(module_mass) for module_mass in get_puzzle_input_as_list("src/day1_input")]
    
    # Computation
    result_part1 = calculate_total_fuel_needed(module_masses)
    result_part2 = calculate_total_fuel_needed2(module_masses)
    
    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()