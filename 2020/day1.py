# --- Day 1: Report Repair ---

from utils import get_puzzle_input_as_list
from itertools import combinations          # combinations is used to get all combinations in an iterable
                                            # + combinations('ABCD', 2) → AB AC AD BC BD CD
                                            # + combinations(range(4), 3) → 012 013 023 123


def main():
    expense_report = [int(expense) for expense in get_puzzle_input_as_list("src/day1_input")]

    # Part 1
    result_part1 = [comb[0] * comb[1] for comb in combinations(expense_report, 2) if sum(comb) == 2020][0]

    # Part 2
    result_part2 = [comb[0] * comb[1] * comb[2]for comb in combinations(expense_report, 3) if sum(comb) == 2020][0]

    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()
