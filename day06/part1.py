from collections import defaultdict
import os
from typing import DefaultDict

State = DefaultDict[int, int]


def update(state: State) -> None:
    # Save the number of fishes that will give birth
    timer_0_fishes = state[0]

    # Those with timer ranging from 1 to 8 will be decreased
    for timer in range(0, 8):
        state[timer] = state[timer + 1]

    # Those with timer = 0 will create new fishes and go back to timer = 6
    state[8] = timer_0_fishes
    state[6] += timer_0_fishes


def parse(input_s: str) -> State:
    state: State = defaultdict(int)
    for timer_s in input_s.strip().split(","):
        state[int(timer_s)] += 1

    return state


def compute(state: State, days: int) -> int:
    for _ in range(days):
        update(state)

    return sum(state.values())


def main() -> int:
    with open(os.path.join("day06", "input.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    state = parse(input_s)
    result = compute(state, days=80)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
