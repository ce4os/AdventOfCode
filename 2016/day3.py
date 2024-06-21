# --- Day 3: Squares With Three Sides ---

from utils import get_puzzle_input_as_list
import re

# Init vars
triangles = get_puzzle_input_as_list("src/day3_input")
valid_triangles_part1 = 0
valid_triangles_part2 = 0

# Part 1
def is_valid_triangle(x: int, y: int, z: int) -> bool:
    """Checks if a triangle is valid"""
    return False if x + y < z or y + z < x or z + x < y else True

# Counting the valid triangles
for triangle in triangles:
    x, y, z = [int(x) for x in re.findall("\d+", triangle)]
    if is_valid_triangle(x, y, z):
        valid_triangles_part1 += 1

# Part 2
column_a, column_b, column_c = [], [], []

# Rearange puzzle input
for triangle in triangles:
    a, b, c = [int(x) for x in re.findall("\d+", triangle)]
    column_a.append(a)
    column_b.append(b)
    column_c.append(c)

def count_valid_triangles(lst: list, idx=0, total=0) -> int:
    """Gets 3 elements of the list, checks is_valid_triangle, if yes counts up and moves to the next three elements"""
    while True:
        x, y, z = lst[idx], lst[idx + 1], lst[idx + 2]
        if is_valid_triangle(x, y, z):
            total += 1
        idx += 3
        if idx == len(lst):
            break
    return total

valid_triangles_column_a = count_valid_triangles(column_a)
valid_triangles_column_b = count_valid_triangles(column_b)
valid_triangles_column_c = count_valid_triangles(column_c)
valid_triangles_part2 = valid_triangles_column_a + valid_triangles_column_b + valid_triangles_column_c

# Results
print("Result Part1: ", valid_triangles_part1)
print("Result Part2: ", valid_triangles_part2)

