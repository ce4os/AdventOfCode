# --- Day 3: Spiral Memory --- 




def build_spiral(location: int) -> dict[int:tuple[int,int]]:
    spiral = {1:(0,0)}
    coordinates = (0,0)
    key = 1
    cycle_length = 1
    cycle = 1
    while location not in spiral:
        for x in range(cycle_length):
            key = key + 1
            coordinates = (coordinates[0] + cycle, coordinates[1])
            spiral[key] = coordinates
        for y in range(cycle_length):
            key = key + 1
            coordinates = (coordinates[0], coordinates[1] + cycle)
            spiral[key] = coordinates
        cycle_length += 1
        cycle *= -1    
    return spiral

def main():
    spiral = build_spiral(347991)
    x, y = spiral[347991]
    result_part1 = abs(x) + abs(y)

    print("Result Part 1: ", result_part1)
    # print("Result Part 2: ", result_part2)



