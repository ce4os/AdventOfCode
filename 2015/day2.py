from utilities import get_puzzle_input_as_list

package_dimensions = get_puzzle_input_as_list("src/day2_input")
total_wrapping_paper = 0
total_ribbon = 0

for package_dimension in package_dimensions:
    # Part 1 - Wrap the box
    length, width, height = [int(side_length) for side_length in package_dimension.split("x")]
    surface_of_box = 2 * length * width + 2 * width * height + 2 * height * length
    area_of_smallest_side = min([length * width, width * height, height * length])
    total_wrapping_paper += surface_of_box + area_of_smallest_side

    # Part 2 - Add ribbons
    bow = length * width * height
    package_dimension = [length, width, height]
    package_dimension.remove(max(package_dimension))
    ribbon = 2*sum(package_dimension)
    total_ribbon += bow + ribbon
    
print(total_wrapping_paper)
print(total_ribbon)
