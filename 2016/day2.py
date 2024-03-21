from utils import get_puzzle_input_as_list

instructions_lst = get_puzzle_input_as_list("src/day2_input")

# Part 1 - Bathroom lock
key_pad = [[1,4,7],[2,5,8],[3,6,9]]
x = 1
y = 1
button = key_pad[x][y]
code = ""

for instructions in instructions_lst:
    for instruction in instructions:
        if instruction == "U":
            if y == 0:
                pass
            else:
                y -= 1
        elif instruction == "D":
            if y == 2:
                pass
            else:
                y += 1    
        elif instruction == "L":
            if x == 0:
                pass
            else:
                x -= 1
        elif instruction == "R":
            if x == 2:
                pass
            else:
                x += 1
    code += str(key_pad[x][y])

# Part 2 - A fancier keypad

key_pad = [[" ", " ","5", " ", " "],
            [" ", "2", "6", "A", " "],
            ["1", "3", "7", "B", "D"],
            [" ", "4", "8", "C", " "],
            [" ", " ", "9", " ", " "]]
x = 0
y = 2
code_part2 = ""

for instructions in instructions_lst:
    for instruction in instructions:
        if instruction == "U":
            if y == 0 or key_pad[x][y - 1] == " ":
                pass
            else:
                y -= 1
        elif instruction == "D":
            if y == 4 or key_pad[x][y + 1] == " ":
                pass
            else:
                y += 1
        elif instruction == "L":
            if x == 0 or key_pad[x - 1][y] == " ":
                pass
            else:
                x -= 1
        elif instruction == "R":
            if x == 4 or key_pad[x + 1][y] == " ":
                pass
            else:
                x += 1
    code_part2 += str(key_pad[x][y])

# Results
print(code)
print(code_part2)