# --- Day 4: Security Through Obscurity ---

import re
from utils import get_puzzle_input_as_list 
from collections import Counter


filename = "day4_demofile.txt"
filename = "day4_data.txt"
rooms = get_puzzle_input_as_list("src/day4_input")
number_of_valid_rooms = 0 
sum_sector_ids = 0
real_rooms = []

for room in rooms:
    checksum = re.search("\[.*\]", room).group()[1:-1]
    sector_id_object = re.search("\d+", room)
    sector_id = sector_id_object.group()
    end_encrypted_name = sector_id_object.start()
    encrypted_name = room[:end_encrypted_name - 1]
    encrypted_name = encrypted_name.replace("-", "")
    cnt = Counter(encrypted_name).most_common()
    lst = []
    sublst = []
    idx = 0
    x = True
    while idx < len(cnt):
        if x:
            value_ = cnt[idx][1]
            x = False
        if cnt[idx][1] == value_:
            sublst.append(cnt[idx])
            idx += 1
            if idx == len(cnt):
                lst.append(sublst)
                break
            else:
                continue
        if cnt[idx][1] != value_:
            lst.append(sublst)
            sublst = []
            x = True
        

    result = []
    for unsorted_lst in lst:
        sorted_lst = sorted(unsorted_lst, key=lambda x: x[0])
        result.extend(sorted_lst)
    lst = []

    real_sum = ""
    for idx in range(5):
        real_sum += result[idx][0]
    if real_sum == checksum:
        real_rooms.append([room[:end_encrypted_name - 1], int(sector_id)])

alphabet = "abcdefghijklmnopqrstuvwxyz"

decrypted_rooms = []
# real_rooms = [["qzmt-zixmtkozy-ivhz", 343]]

for room in real_rooms:
    cipher = room[0]
    cipher = cipher.replace("-", " ")
    rotate_num = room[1]
    num = 0
    while num != rotate_num: 
        decrypted = ""
        for char in cipher:
            if char in alphabet:
                idx = alphabet.index(char)
                if idx == 25:
                    idx = -1
                decrypted += alphabet[idx + 1]
            else:
                decrypted += char
        cipher = decrypted
        num += 1
    decrypted_rooms.append((cipher, rotate_num))

from pprint import pprint
pprint(decrypted_rooms)
# -> python day4.py | grep "north"
