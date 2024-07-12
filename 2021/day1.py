#--- Day 1: Sonar Sweep ---

from utils import get_puzzle_input_as_list


def check_ocean_depth_increases(ocean_depths: list, slide_window: int) -> int:
    """Counts the number of times the ocean depth increases in a given sliding window"""
    count_depth_measurement_increases = 0
    for idx in range(len(ocean_depths) - slide_window):
        A = sum([ocean_depths[idx + x] for x in range(slide_window)])
        B = sum([ocean_depths[idx + x] for x in range(1, slide_window + 1)])
        if A < B: 
            count_depth_measurement_increases += 1
    return count_depth_measurement_increases


def main():
    ocean_depths = [int(depth) for depth in get_puzzle_input_as_list("src/day1_input")]
    result_part1 = check_ocean_depth_increases(ocean_depths, 1)
    result_part2 = check_ocean_depth_increases(ocean_depths, 3)

    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()
