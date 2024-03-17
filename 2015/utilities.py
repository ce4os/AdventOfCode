def get_puzzle_input_as_string(path_to_puzzle_input: str) -> str:
    """Returns content of file as a single string"""
    with open(path_to_puzzle_input) as f:
        content = f.read()
    return content