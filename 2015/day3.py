# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

from utils import get_puzzle_input_as_string


# Get puzzle input
moves = get_puzzle_input_as_string("src/day3_input")


# Part 1 - Instructions from an egnogged elf
def get_visitied_houses(moves: str) -> list:
    """"""
    coordinates = [0,0]
    visited_houses = [(0,0)]
    for move in moves:
        if move == ">":
            coordinates[0] += 1
        elif move == "<":
            coordinates[0] -= 1
        elif move == "^":
            coordinates[1] += 1
        else:
            coordinates[1] -= 1    
        visited_houses.append(tuple(coordinates))
    return visited_houses


houses_visited_by_santa = get_visitied_houses(moves)
number_of_houses_visited = len(set(houses_visited_by_santa))


# Part 2 - With a little help from Robosanta
moves_for_santa = ""
moves_for_robosanta = ""
for counter, char in enumerate(moves):
    if counter%2 == 0:
        moves_for_robosanta += char
    else:
        moves_for_santa += char


houses_visited = get_visitied_houses(moves_for_santa)
houses_visited.extend(get_visitied_houses(moves_for_robosanta))
number_of_houses_visited2 = len(set(houses_visited))


# Results
print("Result Part1: ", number_of_houses_visited)
print("Result Part2: ", number_of_houses_visited2)