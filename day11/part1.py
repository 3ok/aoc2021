import os
from typing import List, Set, Tuple

Grid = List[List[int]]


def print_grid(grid: Grid) -> str:
    print("\n".join("".join(str(n) for n in line) for line in grid) + "\n")


def parse(input_s: str) -> Grid:
    return [[int(c) for c in list(line)] for line in input_s.split("\n")]


def update_grid(grid: Grid) -> int:
    flashes: Set[Tuple[int, int]] = set()
    flashed: Set[Tuple[int, int]] = set()

    # The energy level of each octopus increases by 1
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] += 1
            # Any octopus with an energy level greater than 9 flashes
            if grid[i][j] > 9:
                flashes.add((i, j))

    while flashes:
        i, j = flashes.pop()
        flashed.add((i, j))

        # Loop over adjacent octopuses
        for i_adj in range(max(0, i - 1), min(len(grid), i + 2)):
            for j_adj in range(max(0, j - 1), min(len(grid[0]), j + 2)):
                grid[i_adj][j_adj] += 1
                if grid[i_adj][j_adj] > 9 and (i_adj, j_adj) not in flashed:
                    # This adjacent octopus flashes for the first time this step
                    flashes.add((i_adj, j_adj))
                    flashed.add((i_adj, j_adj))

    # Any octopus that flashed during this step  has its energy level set to 0
    for i, j in flashed:
        grid[i][j] = 0

    return len(flashed)


def compute(grid: Grid, steps: int = 100) -> int:
    n_flashes = 0
    for _ in range(steps):
        n_flashes += update_grid(grid)
    return n_flashes


def main() -> int:
    with open(os.path.join("day11", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    result = compute(parse(input_s))
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
