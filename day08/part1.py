import os
from typing import List, Tuple


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    first, second = line.split(" | ")
    first_digits = first.split()
    second_digits = second.split()
    return first_digits, second_digits


def parse(input_s: str) -> List[Tuple[List[str], List[str]]]:
    return [parse_line(line) for line in input_s.split("\n")]


DIGITS = {
    "0": "abcefg",  # 6
    "1": "cf",  # 2 (unique)
    "2": "acdeg",  # 5
    "3": "acdfg",  # 5
    "4": "bcdf",  # 4 (unique)
    "5": "abdfg",  # 5
    "6": "abdefg",  # 6
    "7": "acf",  # 3 (unique)
    "8": "abcdefg",  # 7 (unique)
    "9": "abcdfg",  # 6
}

def compute(digits : List[str]) -> int:
    n_unique_digits = 0
    for digit in digits:
        if len(digit) in {2, 4, 3, 7}:
            n_unique_digits += 1
            
    return n_unique_digits


def main() -> int:
    with open(os.path.join("day08", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    all_digits = parse(input_s)
    result = 0
    for _, digits in all_digits:
        result += compute(digits)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())