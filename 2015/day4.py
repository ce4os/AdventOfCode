# Day 4: The Ideal Stocking Stuffer

import hashlib

def get_lowest_possible_dec(prefix):
    salt = "bgvyzdsv"
    decimal_number = 1
    while True:
        salted_string = salt + str(decimal_number)
        md5_hash = hashlib.md5(salted_string.encode("utf-8")).hexdigest()
        if md5_hash.startswith(prefix):
            return decimal_number
        else:
            decimal_number += 1

# Results
print(get_lowest_possible_dec("00000"))
print(get_lowest_possible_dec("000000"))

