from typing import List
from typing import Tuple
from itertools import islice
from itertools import product
import os
from copy import deepcopy


Board = List[List[int]]
Filter = List[List[int]]

EMPTY_FILTER: Filter = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def update_filter(board: Board, filter: Filter, number: int) -> None:
    for i, j in product(range(5), range(5)):
        if board[i][j] == number:
            filter[i][j] = 1


def check_win(filter: Filter) -> bool:
    # Check row condition
    for row in filter:
        if sum(row) == 5:
            return True

    # Check column condition
    for j in range(5):
        sum_col = sum(filter[i][j] for i in range(5))
        if sum_col == 5:
            return True

    return False

def compute_score(board: Board, filter: Filter, number: int) -> int:
    s = 0
    for i, j in product(range(5), range(5)):
        if filter[i][j] == 0:
            s += board[i][j]
    
    return s * number
    

def compute(numbers: List[int], boards: List[Board]) -> int:
    filters: List[Filter] = [deepcopy(EMPTY_FILTER) for _ in boards]
    scores: List[int] = []
    for number in numbers:
        for board, filter in zip(boards, filters):
            if not check_win(filter):
                update_filter(board, filter, number)
                win = check_win(filter)
                if win:
                    # We found a winner board, compute the result
                    score = compute_score(board, filter, number)
                    scores.append(score)
    return scores[-1]


def parse(input_s: str) -> Tuple[List[int], List[Board]]:
    lines = input_s.split("\n")

    # First line : numbers to draw
    numbers_str = lines[0].split(",")
    numbers_to_draw = [int(num) for num in numbers_str]

    # Next lines : empty and board lines
    boards: List[Board] = []
    current_board: Board = []
    for line in islice(lines, 2, None, None):
        if line.strip() != "":
            numbers = [int(num) for num in line.strip().split()]
            current_board.append(numbers)
            if len(current_board) == 5:
                boards.append(current_board)
                current_board = []

    return numbers_to_draw, boards


def main() -> int:
    with open(os.path.join("day04", "input2.txt"), "r") as f_in:
        input_s = f_in.read().strip()

    numbers, boards = parse(input_s)
    score = compute(numbers, boards)
    print(score)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
