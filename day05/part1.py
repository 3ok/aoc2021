import os
from typing import Dict, List, Tuple
from itertools import product

Grid = Dict[Tuple[int, int], int]


def parse_line(line: str) -> Tuple[int, int, int, int]:
    first, second, = line.split(" -> ")
    x1, y1 = first.split(",")
    x2, y2 = second.split(",")
    return int(x1), int(y1), int(x2), int(y2)

def create_grid(max_x: int, max_y: int) -> Grid:
    return {(x, y): 0 for x, y in product(range(max_x+1), range(max_y+1))}

def update_grid(grid: Grid, x1:int, y1: int, x2: int, y2:int) -> None:
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    if min_x == max_x:
        # Horizontal line
        for y in range(min_y, max_y + 1):
            grid[(min_x, y)] += 1
    elif min_y == max_y:
        # Vertical line
        for x in range(min_x, max_x + 1):
            grid[(x, min_y)] += 1
    else:
        # We can't draw an horizontal or vertical line : do nothing
        # raise AssertionError(f"Can't draw line between ({x1},{y1}) and ({x2},{y2})")
        pass

def compute_score(grid: Grid) -> int:
    score = 0
    for v in grid.values():
        if v >= 2:
            score += 1
    return score


def parse(input_s: str) -> List[Tuple[int, int, int, int]]:
    return [parse_line(line) for line in input_s.split("\n")]

def compute(lines: List[Tuple[int, int, int, int]]) -> int:
    max_x = max(max(line[0] for line in lines), max(line[2] for line in lines))
    max_y = max(max(line[1] for line in lines), max(line[3] for line in lines))
    grid = create_grid(max_x, max_y)
    for x1, y1, x2, y2 in lines:
        update_grid(grid, x1, y1, x2, y2)
    
    return compute_score(grid)


def main() -> int:
    with open(os.path.join("day05", "input1.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    lines = parse(input_s)
    score = compute(lines)
    print(score)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())