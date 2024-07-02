# --- Day 1: Inverse Captcha ---

from utils import get_puzzle_input_as_string
sequence_of_digits = get_puzzle_input_as_string("src/day1_input")

# Part 1

def get_sum_of_all_digits_that_match_the_next_digit(sequence_of_digits: str) -> int:
    sum = 0
    for idx, num in enumerate(sequence_of_digits):
        try: 
            if num == sequence_of_digits[idx + 1]:
                sum += int(num)
        except IndexError:
            if num == sequence_of_digits[0]:
                sum += int(num)
    return sum

result_part1 = get_sum_of_all_digits_that_match_the_next_digit(sequence_of_digits)

# Part 2

def get_sum_of_all_digits_that_match_the_digit_halfway_around_the_circular_list(sequence_of_digits: str) -> int:
    sum = 0
    # construct a pseudo circular list
    halfway = int(len(sequence_of_digits)/2)
    pseudo_circular_sequence = sequence_of_digits + sequence_of_digits[:halfway] 
    for idx, num in enumerate(sequence_of_digits):
        if num == pseudo_circular_sequence[idx + halfway]:
            sum += int(num)
    return sum

result_part2 = get_sum_of_all_digits_that_match_the_digit_halfway_around_the_circular_list(sequence_of_digits)

print("Result Part1: ", result_part1)
print("Result Part2: ", result_part2)


