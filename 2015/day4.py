# --- Day 4: The Ideal Stocking Stuffer ---

import hashlib


# Define function
def get_lowest_possible_dec(prefix: str, salt: str, decimal: int) -> str:
    """Calculates md5 hash of salt+dec; returns decimal if hash startswith prefix, else dec += 1"""
    while True:
        salted_string = salt + str(decimal)
        md5_hash = hashlib.md5(salted_string.encode("utf-8")).hexdigest()
        if md5_hash.startswith(prefix):
            return decimal
        else:
            decimal += 1


# Results
print("Result Part 1: ", get_lowest_possible_dec("00000", "bgvyzdsv", 1))
print("Result Part 2: ", get_lowest_possible_dec("000000", "bgvyzdsv", 1))

