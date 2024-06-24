# --- Day 6: Probably a Fire Hazard ---

import re
from utils import get_puzzle_input_as_list

instructions = get_puzzle_input_as_list("src/day6_input")

def build_rectangle(min_x: int, max_x: int, min_y:int, max_y:int) -> list:
    """Builds a rectangle with inclusive ranges"""
    rectangle = []
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            rectangle.append((y,x))
    return rectangle

grid_without_states = build_rectangle(0, 1000, 0, 1000)

# statefull grid connects coordinates with state of the light and its brightness
# coordinate:[state, brightness]
grid = {light_coordinates: [-1, 0] for light_coordinates in grid_without_states}


# processing instructions
for instruction in instructions:
    corners = [int(x) for x in re.findall("\d+", instruction)]
    rectangle = build_rectangle(corners[0], corners[2] + 1, corners[1], corners[3] + 1)
    for key in rectangle:
        if "toggle" in instruction:
            grid[key][0] *= -1
            grid[key][1] += 2
        elif "turn off" in instruction:
            grid[key][0] = -1
            if grid[key][1] > 0:
                grid[key][1] -= 1 
        else:
            grid[key][0] = 1
            grid[key][1] += 1

result_part1 = 0
total_brightness = 0
for state in grid.values():
    if state[0] == 1:
        result_part1 += 1
    total_brightness += state[1]
    

# Results
print("Results Part 1: ", result_part1)
print("Results Part 2: ", total_brightness)



    
    




    
    

