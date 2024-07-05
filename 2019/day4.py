# --- Day 4: Secure Container ---

def check_for_two_equal_adjacent_digits(password: str) -> bool:
    for idx, digit in enumerate(password):
        if idx == 5:
            return False
        if digit == password[idx + 1]:
            return True
    
def check_for_decreasing_digits(password: str) -> bool:
    for idx, digit in enumerate(password):
        if idx == 5:
            return True
        if int(digit) > int(password[idx + 1]):
            return False

def count_valid_passwords() -> int:
    valid_passwords = 0
    for password in range(138307, 654505):
        password = str(password)
        if check_for_decreasing_digits(password) and check_for_two_equal_adjacent_digits(password):
            valid_passwords += 1
    return valid_passwords
 
def main():
    # Init
    # Part 1
    

    result_part1 = count_valid_passwords()
    result_part2 = 0 
    # Results
    print("Result Part 1: ", result_part1)
    print("Result Part 2: ", result_part2)


if __name__ == "__main__":
    main()