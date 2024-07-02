# --- Day 1: Inverse Captcha ---

from utils import get_puzzle_input_as_string
sequence_of_digits = get_puzzle_input_as_string("src/day1_input")

# Part 1

def get_sum_of_all_digits_that_match_the_next_digit(sequence_of_digits: str) -> int:
    sum = 0
    for idx, num in enumerate(sequence_of_digits):      #
        try:                                            # try-except block to catch index error when last digit is reached [idx + 1]
            if num == sequence_of_digits[idx + 1]:      # check if digit equals next digit
                sum += int(num)                         #
        except IndexError:                              # if the end of the list is reached, check 
            if num == sequence_of_digits[0]:            #+ if last digit matches first digit
                sum += int(num)                         #
    return sum                                          #

result_part1 = get_sum_of_all_digits_that_match_the_next_digit(sequence_of_digits)

# Part 2

def get_sum_of_all_digits_that_match_the_digit_halfway_around_the_circular_list(sequence_of_digits: str) -> int:
    sum = 0
    halfway = int(len(sequence_of_digits)/2)                                        # 
    pseudo_circular_sequence = sequence_of_digits + sequence_of_digits[:halfway]    # construct a pseudo circular sequence
    for idx, num in enumerate(sequence_of_digits):
        if num == pseudo_circular_sequence[idx + halfway]:
            sum += int(num)
    return sum

result_part2 = get_sum_of_all_digits_that_match_the_digit_halfway_around_the_circular_list(sequence_of_digits)

print("Result Part1: ", result_part1)
print("Result Part2: ", result_part2)


