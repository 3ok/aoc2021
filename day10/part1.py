import os
from typing import List

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def parse(input_s: str) -> List[str]:
    return input_s.split("\n")


def compute_line(line: str) -> int:
    stack: List[str] = [line[0]]
    for char in line[1:]:
        if char in PAIRS:
            stack.append(char)
        else:
            last_open = stack.pop(-1)
            if char != PAIRS[last_open]:
                return SCORES[char]
    return 0


def main() -> int:
    with open(os.path.join("day10", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    lines = parse(input_s)
    scores = []
    for line in lines:
        scores.append(compute_line(line))
    print(sum(scores))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
