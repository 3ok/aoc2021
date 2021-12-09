import os
from typing import List
from itertools import product

Grid = List[List[int]]


def parse(input_s: str) -> Grid:
    return [[int(val) for val in line] for line in input_s.split("\n")]


def is_lowest(grid: Grid, i: int, j: int) -> bool:
    x_max = len(grid)
    y_max = len(grid[0])
    value = grid[i][j]
    
    range_x = range(max(0, i - 1), min(x_max, i + 2))
    range_y = range(max(0, j - 1), min(y_max, j + 2))
    
    min_value = min(grid[x][y] for x, y in product(range_x, range_y))
    
    if min_value == value:
        return True
    else:
        return False

def compute(grid: Grid) -> int:
    lowest_points: List[int] = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if is_lowest(grid, i, j):
                lowest_points.append(val)
    return sum([lowest_point + 1 for lowest_point in lowest_points])


def main() -> int:
    with open(os.path.join("day09", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    
    grid = parse(input_s)
    result = compute(grid)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())