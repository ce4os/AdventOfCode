from utils import get_puzzle_input_as_list#
import re

triangles = get_puzzle_input_as_list("src/day3_input")

valid_triangles_part1 = 0
valid_triangles_part2 = 0
triangle_a, triangle_b, triangle_c = [], [], []

def is_valid_triangle(a, b, c):
    return (a + b > c and b + c > a and a + c > b) 

for counter, triangle in enumerate(triangles):
    a, b, c = [int(x) for x in re.findall("\d+", triangle)]
    # Part1 - counting valid triangles
    if is_valid_triangle(a, b, c):
        valid_triangles_part1 += 1

    # Part2 - validating vertical triangles
    triangle_a.append(a), triangle_b.append(b), triangle_c.append(c)
    if (counter + 1) % 3 == 0:
        vertical_triangles = [triangle_a, triangle_b, triangle_c]
        for triangle in vertical_triangles:
            a, b, c = triangle
            if is_valid_triangle(a, b, c):
                valid_triangles_part2 += 1
        triangle_a, triangle_b, triangle_c = [], [], []
        
# Results
print(valid_triangles_part1)
print(valid_triangles_part2)

