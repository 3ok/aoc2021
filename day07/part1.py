import os
from typing import Dict, List, Optional


def parse(input_s) -> List[int]:
    return [int(x) for x in input_s.split(",")]


def compute_score(positions: List[int], final_position: int) -> int:
    return sum(abs(pos - final_position) for pos in positions)


def compute(positions: List[int]) -> float:
    scores: Dict[int, int] = {}
    max_position, min_position = max(positions), min(positions)
    min_score: Optional[int] = None
    best_position = 0
    for final_position in range(min_position, max_position + 1):
        score = compute_score(positions, final_position)
        scores[final_position] = score
        if min_score is None or score < min_score:
            min_score = score
            best_position = final_position
    return best_position, min_score


def main() -> int:
    with open(os.path.join("day07", "input.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    best_position, min_score = compute(parse(input_s))
    print(best_position)
    print(min_score)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
