# --- Day 2: 1202 Program Alarm ---

from utils import get_puzzle_input_as_string


# Functions Part 1
def execute_intcode_program(
    intcode_program: list[int], instruction_pointer: int, noun: int, verb: int
) -> int:
    """Executes the given Intcode program with specified noun and verb."""
    intcode_program[1] = noun
    intcode_program[2] = verb
    while True:
        opcode = intcode_program[instruction_pointer]
        input1_position = intcode_program[instruction_pointer + 1]
        input2_position = intcode_program[instruction_pointer + 2]
        output_position = intcode_program[instruction_pointer + 3]
        if opcode == 1:
            output_value = (
                intcode_program[input1_position] + intcode_program[input2_position]
            )
        elif opcode == 2:
            output_value = (
                intcode_program[input1_position] * intcode_program[input2_position]
            )
        elif opcode == 99:
            return intcode_program[0]
        intcode_program[output_position] = output_value
        instruction_pointer += 4


# Functions Part 2
def reset_memory():
    """Reset the memory to initial state"""
    return [
        int(integer)
        for integer in get_puzzle_input_as_string("src/day2_input").split(",")
    ]


def find_noun_and_verb():
    """Returns searched for noun and verb by going through every possible combination"""
    for noun in range(0, 100):
        for verb in range(0, 100):
            intcode_program = reset_memory()
            if execute_intcode_program(intcode_program, 0, noun, verb) == 19690720:
                return 100 * noun + verb


def main():
    # Init
    intcode_program = [
        int(integer)
        for integer in get_puzzle_input_as_string("src/day2_input").split(",")
    ]

    # Computation
    result_part1 = execute_intcode_program(intcode_program, 0, 12, 2)
    result_part2 = find_noun_and_verb()

    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()
