# --- Day 1: Not Quite Lisp ---

from utils import get_puzzle_input_as_string


# Get puzzle input
directions = get_puzzle_input_as_string("src/day1_input")


# Part 1 - Santa delivers presents in a large appartement building
def process_instructions(directions: str) -> int:
    floor = sum([1 if char == "(" else -1 for char in directions])
    return floor


# Part 2 - Santa in the basement
def process_instructions2(directions: str) -> int:
    floor = 0
    for position, char in enumerate(directions):
        if char == "(": 
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return position + 1


# Results
print("Result Part1: ", process_instructions(directions))
print("Result Part2: ", process_instructions2(directions))