from typing import List
from itertools import islice
import os


def compute(numbers: List[int]) -> int:
    if len(numbers) <= 1:
        return 0
    n_increases = 0
    previous_numbers = islice(numbers, None, len(numbers) - 1)
    current_numbers = islice(numbers, 1, None)
    for previous_number, current_number in zip(previous_numbers, current_numbers):
        if current_number > previous_number:
            n_increases += 1
    return n_increases


def parse(input_s: str) -> List[int]:
    return [int(line) for line in input_s.split()]


def main() -> int:
    with open(os.path.join("day01", "input1.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    numbers = parse(input_s)
    result = compute(numbers)
    print(result)

    return 0

if __name__ == "__main__":
    raise SystemExit((main()))