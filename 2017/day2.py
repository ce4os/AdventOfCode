# --- Day 2: Corruption Checksum ---

import re
from utils import get_puzzle_input_as_list

spread_sheet = get_puzzle_input_as_list("src/day2_input")

# Part 1

def get_values(string_with_integers):
    """finds all numbers in a given string and returns them as a list of ints"""
    return [int(x) for x in re.findall("\d+", string_with_integers)]

def calculate_difference_of_lowest_and_highest_value(list_of_integers: list) -> int:
    """Calculates the difference of the highest and lowest value of a list of ints"""
    return max(list_of_integers) - min(list_of_integers)

def get_quotient_of_numbers_dividing_without_rest(list_of_integers: list):
    sorted_list = sorted(list_of_integers)
    sorted_list.reverse()
    for dividend in sorted_list:
        for divisor in sorted_list:
            if dividend != divisor and dividend % divisor == 0:
                return int(dividend / divisor)
    return 0


def get_get_results_part1_and_part2(spreadsheet: str):
    checksum1 = 0
    checksum2 = 0
    for row in spread_sheet:
        all_values = get_values(row)
        checksum1 += calculate_difference_of_lowest_and_highest_value(all_values)
        checksum2 += get_quotient_of_numbers_dividing_without_rest(all_values) 
    return checksum1, checksum2

result_part1, result_part2 = get_get_results_part1_and_part2(spread_sheet)

# Part 2


print("Result Part1: ", result_part1)
print("Result Part2: ", result_part2)
