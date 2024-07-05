# --- Day 3: Crossed Wires ---

from utils import get_puzzle_input_as_list

def create_wire_coordinates(path: str) -> list[(int,int)]:
    coordinates = (0,0)
    path_coordinates = []
    directions = path.split(",")
    for direction_and_distance in directions:
        direction = direction_and_distance[0]
        distance = int(direction_and_distance[1:])
        if direction == "R":
            for step in range(distance):
                 new_coordinates = (coordinates[0] + 1, coordinates[1])
                 coordinates = new_coordinates
                 path_coordinates.append(coordinates)
        elif direction == "U":
            for step in range(distance):
                new_coordinates = (coordinates[0], coordinates[1] + 1)
                coordinates = new_coordinates
                path_coordinates.append(coordinates)
        elif direction == "L":
            for step in range(distance):
                new_coordinates = (coordinates[0] - 1, coordinates[1])
                coordinates = new_coordinates
                path_coordinates.append(coordinates)
        elif direction == "D":
            for step in range(distance):
                new_coordinates = (coordinates[0], coordinates[1] - 1)
                coordinates = new_coordinates
                path_coordinates.append(coordinates)
    return path_coordinates
            

def get_intersection_coordinates(path_wire1: list[(int,int)], path_wire2: list[(int,int)]) -> list[(int,int)]:
    intersections = []
    path_wire1 = set(path_wire1)                # conversion to sets for fast membership test
    path_wire2 = set(path_wire2)                #+
    for coordinates in path_wire1:
        if coordinates in path_wire2:
            intersections.append(coordinates)
    return intersections

def get_shortest_manhatten_distance(intersections: list[(int,int)]) -> int:
    return  min([abs(x) + abs(y) for x,y in intersections])
    


def main():
    # Init
    path_wire1, path_wire2 = get_puzzle_input_as_list("src/day3_input")
    # Part 1
    path_wire1 = create_wire_coordinates(path_wire1)
    path_wire2 = create_wire_coordinates(path_wire2)
    intersection_coordinates = get_intersection_coordinates(path_wire1, path_wire2)
    result_part1 = get_shortest_manhatten_distance(intersection_coordinates) 
    
    result_part2 = 0
    
    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()