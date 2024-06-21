# --- Day 2: Bathroom Security ---

from utils import get_puzzle_input_as_list 

# Initialize vars
instructions_lst = get_puzzle_input_as_list("src/day2_input")
key_pad = [[1,4,7],[2,5,8],[3,6,9]]
key_pad2 = [
    [" ", " ","5", " ", " "],
    [" ", "2", "6", "A", " "],
    ["1", "3", "7", "B", "D"],
    [" ", "4", "8", "C", " "],
    [" ", " ", "9", " ", " "]
]
x, y = 1, 1
button = key_pad[1][y]
result_part1 = ""
result_part2 = ""

# Part 1
for instructions in instructions_lst:
    for instruction in instructions:
        if instruction == "U":
            if y != 0:
                y -= 1
        elif instruction == "D":
            if y != 2:
                y += 1
        elif instruction == "L":
            if x != 0:
                x -= 1
        elif instruction == "R":
            if x != 2:
                x += 1
    result_part1 += str(key_pad[x][y])


# Part 2
# Reinit x,y 
x, y = 0, 2

for instructions in instructions_lst:
    for instruction in instructions:
        if instruction == "U":
            if y != 0 and key_pad2[x][y - 1] != " ":
                y -= 1
        elif instruction == "D":
            if y != 4 and key_pad2[x][y + 1] != " ":
                y += 1
        elif instruction == "L":
            if x != 0 and key_pad2[x - 1][y] != " ":
                x -= 1
        elif instruction == "R":
            if x != 4 and key_pad2[x + 1][y] != " ":
                x += 1
    result_part2 += str(key_pad2[x][y])

print("Result Part1: ", result_part1)
print("Result Part2: ", result_part2)
