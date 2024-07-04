# --- Day 1: Chronal Calibration ---

import re
from utils import get_puzzle_input_as_string

def main():
    # Part 1
    result_part1 = 0
    result_part2 = None
    # get puzzle input as string and convert every positive or negative number to its respective integer
    list_of_frequency_changes = [int(x) for x in re.findall(r"[+-]\d+", get_puzzle_input_as_string("src/day1_input"))]
    result_part1 = sum(list_of_frequency_changes)           # summarize all integers in list
    
    # Part 2
    memory = []                                             ## init memory & frequency
    frequency = 0                                           #+ 
    while True:                                             #+ Add frequencies to memory until one repeats, if list of frequency changes is exhausted, start anew
        for frequency_change in list_of_frequency_changes:  #+ calculate frequency
            memory.append(frequency)                        #+ add to memory
            frequency += frequency_change                   #+ calculate new frequency
            if frequency in memory:                         #+ check if in memory
                result_part2 = frequency                    #+ if yes, break for loop
                break  
        if result_part2:                                    #+ if frequency reoccured, break while loop
            break
    
    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()