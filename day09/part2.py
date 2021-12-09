import os
from typing import List, Tuple
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


def find_basin_from(mask_grid: Grid, i: int, j: int) -> int:
    x_max = len(mask_grid)
    y_max = len(mask_grid[0])

    basin_size = 0
    if mask_grid[i][j] == 0:
        # Mark it
        mask_grid[i][j] = 1
        basin_size = 1
        if i > 0:
            basin_size += find_basin_from(mask_grid, i - 1, j)
        if i < x_max - 1:
            basin_size += find_basin_from(mask_grid, i + 1, j)
        if j > 0:
            basin_size += find_basin_from(mask_grid, i, j - 1)
        if j < y_max - 1:
            basin_size += find_basin_from(mask_grid, i, j + 1)

    return basin_size


def compute(grid: Grid) -> int:
    mask_grid: Grid = []
    for row in grid:
        mask_row = [9 if val == 9 else 0 for val in row]
        mask_grid.append(mask_row)

    basins: List[int] = []
    for i, row in enumerate(mask_grid):
        for j, _ in enumerate(row):
            basins.append(find_basin_from(mask_grid, i, j))

    three_biggest_basins = sorted(basins, reverse=True)[:3]

    return three_biggest_basins[0] * three_biggest_basins[1] * three_biggest_basins[2]


def main() -> int:
    with open(os.path.join("day09", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    grid = parse(input_s)
    result = compute(grid)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
