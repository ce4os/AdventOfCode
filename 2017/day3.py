# --- Day 3: Spiral Memory --- 

# Part 1
## Step 1:
# Build spiral
# Start at[1:(0,0)]
# Cycle 1 +
# one to the right, one up
# [2:(1,0), 3:(1,1)]
# Cycle 2 - 
# two to the left, two down
# [4:(0,1), 5:(-1,1), 6:(-1,0), 7:(-1,-1)]
# Cycle 3 + 
# three to the right, three up
# [8:(0,-1), 9:(1,-1), 10:(2,-1) ... 13(2,2)]
# Cycle 4 -
# four to the left, four down
# [14:(1, 2) ... 21(-2,-2)]

spiral = {1:(0,0)}
key = 1
cycle = 1
while 21 not in spiral:
    latest_coordinates = spiral[key]
    print(latest_coordinates)
    for x in range(cycle):
        next_key = key + 1
        next_coordinates = (latest_coordinates[0] + cycle, latest_coordinates[1])
        spiral[next_key] = next_coordinates
        key = next_key
    latest_coordinates = spiral[key]
    for y in range(cycle):
        next_key = key + 1
        next_coordinates = (latest_coordinates[0], latest_coordinates[1] + cycle)
        spiral[next_key] = next_coordinates
        key = next_key
    cycle *= -1
    if cycle < 0:
        cycle = cycle - 1
    else:
        cycle = cycle + 1

print(spiral)
    
    

