from utils import get_puzzle_input_as_string

directions = get_puzzle_input_as_string("src/day1_input")

# Part 1 - Santa delivers presents in a large appartement building
def process_instructions(directions: str):
    floor = sum([1 if char == "(" else -1 for char in directions])
    return floor

# Part 2 - Santa in the basement
def process_instructions2(directions: str):
    floor = 0
    for position, char in enumerate(directions):
        if char == "(": 
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return position + 1

# Results
print(process_instructions(directions))
print(process_instructions2(directions))