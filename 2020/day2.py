# --- Day 2: Password Philosophy ---

import re
from typing import Callable
from utils import get_puzzle_input_as_list


def get_parameters(policy_and_password: str) -> tuple:
    """Extracts range, letter and password from policy_and_password"""
    param1, param2 = [int(param) for param in re.search("\d+-\d+", policy_and_password).group().split("-")]
    letter = re.search("(?<= )\w+(?=:)", policy_and_password).group()
    password = policy_and_password.split(" ")[2]
    return (param1, param2, letter, password)


def tobbogan_interpreter(position1: int, position2: int, letter: str, password: str) -> bool:
    """Checks if exactly one of these positions contains the given letter."""
    letter_pos1, letter_pos2 = password[position1 - 1], password[position2 - 1]
    return (letter_pos1 == letter and not letter_pos1 == letter_pos2) or (
        letter_pos2 == letter and not letter_pos2 == letter_pos1
    )


def sled_rental_interpreter(minimum: int, maximum: int, letter: str, password: str) -> bool:
    """Checks if letter within inclusive range of maximum and minimum"""
    return minimum <= password.count(letter) <= maximum


def count_valid_passwords(list_of_policies_and_passwords: list, interpreter: Callable) -> int:
    """Checks if passwords are in line with given policy depending on the interpreter"""
    return  sum([1 for policy_password in list_of_policies_and_passwords if interpreter(*get_parameters(policy_password)) is True])


def main() -> None:
    list_of_policies_and_passwords = get_puzzle_input_as_list("src/day2_input")
    result_part1 = count_valid_passwords(list_of_policies_and_passwords, sled_rental_interpreter)
    result_part2 = count_valid_passwords(list_of_policies_and_passwords, tobbogan_interpreter)

    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()
