# --- Day 4: Security Through Obscurity ---

import re
from collections import Counter
from utils import get_puzzle_input_as_list 


rooms = get_puzzle_input_as_list("src/day4_input")
result_part1 = 0
result_part2 = 0


def get_checksum(room: str) -> str:
    """Searches and returns checksum of a room"""
    return re.search("(?<=\[)\w+(?=\])", room).group()


def get_encrypted_name(room: str) -> str:
    """Searches and returns the encrypted name of a room"""
    encrypted_name_with_dashes = re.search("^[a-z].*-(?=[0-9])", room).group()
    return encrypted_name_with_dashes[:-1]


def get_sector_id(room: str) -> int:
    """Searches and returns the sector id of a room as an int"""  
    return int(re.search("\d+", room).group())


def get_effective_checksum(encrypted_room_name: str) -> str:
    "Builds a string of the five most common letters in encrypted_room_name"
    most_common_letters = Counter(encrypted_room_name).most_common()
    sorted_five_most_common_letters = sorted(most_common_letters, key=lambda x: (-x[1], x[0]))[:5]
    effective_checksum = "".join([x[0] for x in sorted_five_most_common_letters])
    return effective_checksum


# Part 2
def decrypt_room_name(encrypted_room_name: str, shift: int) -> str:
    """Shifts every alphabetic char in a string by shift and returns decrypted text"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_room_name = ""
    if shift > 26:
        shift = shift % 26
    for char in encrypted_room_name: 
        if char.isalpha():
            cipher_alphabet = alphabet[alphabet.index(char):] + alphabet[:alphabet.index(char)]
            shifted_char = cipher_alphabet[cipher_alphabet.index(char) + shift]
            decrypted_room_name += shifted_char
        else:
            decrypted_room_name += char
    return decrypted_room_name


def calculate_sum_of_sector_ids(list_of_rooms: list) -> int:
    """Calculates sum of sector ids"""
    sum_of_sector_ids = 0
    for room in list_of_rooms:
        encrypted_room_name = get_encrypted_name(room).replace("-", "")
        effective_checksum = get_effective_checksum(encrypted_room_name)
        real_checksum = get_checksum(room)
        if effective_checksum == real_checksum:
            sector_id = get_sector_id(room)
            sum_of_sector_ids += sector_id 
    return sum_of_sector_ids


def is_room_with_northpole_objects(decrypted_room_name):
    """Returns true if decrypted room name contains 'north' else False"""
    return True if "north" in decrypted_room_name else False


def get_result_part_two(list_of_rooms: list) -> int:
    """Checks if room is real room, if true decrypts room name and checks if 'north' in name."""
    for room in list_of_rooms:
        encrypted_room_name = get_encrypted_name(room).replace("-", "")
        effective_checksum = get_effective_checksum(encrypted_room_name)
        real_checksum = get_checksum(room)
        if effective_checksum == real_checksum:
            sector_id = get_sector_id(room)
            decrypted_room_name = decrypt_room_name(encrypted_room_name, sector_id)
            if is_room_with_northpole_objects(decrypted_room_name):
                result_part2 = get_sector_id(room)
                return result_part2



print("Result Part1: ", calculate_sum_of_sector_ids(rooms))
print("Result Part2", get_result_part_two(rooms))




    







