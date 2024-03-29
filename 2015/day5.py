#TODO: Refactor!

import re
from utils import get_puzzle_input_as_list

# Part 1 - Naughty or nice?
santas_strings = get_puzzle_input_as_list("src/day5_input")
nice_strings = 0

for string in santas_strings:
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        continue
    if len(re.findall("[aeiou]", string)) < 3:
        continue
    if len(re.findall(r"(.)\1", string)) == 0:
        continue
    nice_strings += 1

# Part 2 - New rules
nice_strings2 = 0
for string in santas_strings:
    pair_appears_twice = False
    repeating_letter = False
    start = 0
    end = 2
    while True:
        pair = string[start:end]
        triplet = string[start:end + 1]
        if len(triplet) != 3: 
            break
        if triplet[0] == triplet[2]:
            repeating_letter = True 
        segment = string[end:]
        if pair in segment:
            pair_appears_twice = True
        start += 1
        end += 1
    if pair_appears_twice and repeating_letter:
        nice_strings2 += 1
        
# Results
print(nice_strings)
print(nice_strings2)


