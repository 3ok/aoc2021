import os
from typing import List

SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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
    score = 0
    for char in line[1:]:
        if char in PAIRS:
            stack.append(char)
        else:
            last_open = stack.pop(-1)
            if char != PAIRS[last_open]:
                # Corrupted line, ignore it
                return 0
    # The remaining characters in the stack are the missing ones
    missing_chars = [PAIRS[char] for char in stack]
    for missing_char in reversed(missing_chars):
        score *= 5
        score += SCORES[missing_char]
    return score


def main() -> int:
    with open(os.path.join("day10", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    lines = parse(input_s)
    scores: List[int] = []
    for line in lines:
        score = compute_line(line)
        if score != 0:
            scores.append(score)
    
    n_scores = len(scores)
    print(sorted(scores)[n_scores // 2])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
