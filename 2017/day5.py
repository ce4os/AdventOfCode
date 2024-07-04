# --- Day 5: A Maze of Twisty Trampolines, All Alike ---

from utils import get_puzzle_input_as_list
from copy import deepcopy

def calculate_steps_to_escape(maze: list[int], puzzle_part: int) -> int:
    """Calculates the number of steps required to escape the maze"""
    steps = 0
    position = 0 
    while True:
        try:
            offset = maze[position]
        except IndexError:              # ending condition
            break
        new_position = position + maze[position]        
        if puzzle_part == 1:            # condition for offset increase for puzzle_part 1
            maze[position] += 1
        if puzzle_part == 2:            # conditions for offset increase for puzzle_part 2
            if maze[position] >= 3:
                maze[position] -= 1
            else:
                maze[position] += 1
        position = new_position
        steps += 1
    return steps


def main():
    maze1 = [int(x) for x in get_puzzle_input_as_list("src/day5_input")]  # cast every jump offsets to int
    maze2 = deepcopy(maze1)
    result_part1 = calculate_steps_to_escape(maze1, 1)
    result_part2 = calculate_steps_to_escape(maze2, 2)
    print("Result Part1: ", result_part1)
    print("Result Part2: ", result_part2)

if __name__ == "__main__":
    main()