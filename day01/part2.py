from typing import List
from itertools import islice
import os

def compute(numbers: List[int]) -> int:
    if len(numbers) <= 3:
        return 0
    
    n_increases = 0
    for i, current_number in islice(enumerate(numbers), 2, len(numbers) - 1):
        current_sum = current_number + numbers[i-1] + numbers[i+1]
        previous_sum = numbers[i-2] + numbers[i-1] + current_number
        if current_sum > previous_sum:
            n_increases += 1
    return n_increases


def parse(input_s: str) -> List[int]:
    return [int(line) for line in input_s.split()]


def main() -> int:
    with open(os.path.join("day01", "input2.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    numbers = parse(input_s)
    result = compute(numbers)
    print(result)

    return 0

if __name__ == "__main__":
    raise SystemExit((main()))