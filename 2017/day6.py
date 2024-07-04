# --- Day 6: Memory Reallocation ---

import re
from copy import deepcopy
from utils import get_puzzle_input_as_string


def do_memory_allocation_routine(memory_banks: list[int]) -> list[int]:
    """"""
    blocks = max(memory_banks)                                                  ##  find number of most blocks
    index_memory_bank_with_most_blocks = memory_banks.index(blocks)             #+ find index of memory bank with most blocks
    memory_banks[index_memory_bank_with_most_blocks] = 0                        #  remove all blocks from selected bank
    index = index_memory_bank_with_most_blocks + 1                              #  move to next memory bank
    for block in range(blocks):                                                 ## start inserting one block per bank
        try:                                                                    #+
            memory_banks[index] += 1                                            #+
        except IndexError:                                                      #+
            index = 0                                                           #+
            memory_banks[index] += 1                                            #+
        index += 1                                                              #+
    return memory_banks


def main() -> None:
    # Part 1
    result_part1 = 0
    configuration_memory = []
    memory_banks = [int(bank) for bank in re.findall(r"\d+", get_puzzle_input_as_string("src/day6_input"))]
    while memory_banks not in configuration_memory:
        configuration_memory.append(deepcopy(memory_banks))                         ## remember configuration to detect infinite loop
        memory_banks = do_memory_allocation_routine(memory_banks)
        result_part1 += 1
    # Part 2
    memory_bank_first_seen_at = configuration_memory.index(memory_banks)            ## Find location where last configuration first occured
    total_length_before_infinite_loop = len(configuration_memory)                   ## Find out total length of allocation to calculate how many cycles are inbetween
    result_part2 = total_length_before_infinite_loop - memory_bank_first_seen_at
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()
