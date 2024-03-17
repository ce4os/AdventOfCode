from utilities import get_puzzle_input_as_string

# Part 1 - Santa delivers presents in a large appartement building

instructions = get_puzzle_input_as_string("day1_input.txt")
def process_instructions(instructions: str):
    floor = sum([1 if char == "(" else -1 for char in instructions])
    return floor

santas_floor = process_instructions(instructions)
print(santas_floor)

# Part 2 - Santa in the basement
def process_instructions2(instructions: str):
    floor = 0
    for position, char in enumerate(instructions):
        if char == "(": 
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return position

position = process_instructions2(instructions)

# enumerate starts at idx 0
position += 1
print(position)