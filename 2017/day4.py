# --- Day 4: High-Entropy Passphrases ---

import re
from collections import Counter
from itertools import combinations
from utils import get_puzzle_input_as_list


# Functions for Part 1

def get_all_words_of_a_passphrase(passphrase: str) -> list:
    """Parses a string and returns all words in string"""
    return re.findall(r"\w+", passphrase)


def passphrase_contains_duplicates(passphrase_as_list_words: list) -> bool:
    """Checks if duplicate words in string"""
    return len(set(passphrase_as_list_words)) != len(passphrase_as_list_words)      # set only contains uniq values. If len == length of original list -> no duplicates


# Functions for Part 2

def is_anagram(word1: str, word2: str) -> bool:
    """Checks if two strings are anagrams returns True if so"""
    return Counter(word1) == Counter(word2)


def passphrase_contains_anagram(passphrase_as_list_of_words: list) -> bool:
    """Checks if a list of words contains an anagram returns true if so"""  
    all_combinations = [combination for combination in combinations(passphrase_as_list_of_words, 2)]    #       
    return any([is_anagram(comb[0], comb[1]) for comb in all_combinations])

    
def main():
    result_part1 = 0
    result_part2 = 0
    passphrases = get_puzzle_input_as_list("src/day4_input")
    for passphrase in passphrases:
        words = get_all_words_of_a_passphrase(passphrase)
        if not passphrase_contains_duplicates(words):
            result_part1 += 1
        if not passphrase_contains_anagram(words):
            result_part2 += 1
    print("Result Part1: ", result_part1)
    print("Result Part2: ", result_part2)


if __name__ == "__main__":
    main()