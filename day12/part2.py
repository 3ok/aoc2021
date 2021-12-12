import os
from collections import Counter, defaultdict
from typing import DefaultDict, List, Set, Tuple


def parse_line(line: str) -> Tuple[str, str]:
    (
        first,
        second,
    ) = line.split("-")
    return first, second


def parse(input_s: str) -> DefaultDict[str, Set[str]]:
    mapping: DefaultDict[str, Set[str]] = defaultdict(set)
    for line in input_s.split("\n"):
        first, second = parse_line(line)
        mapping[first].add(second)
        mapping[second].add(first)

    return mapping


def is_small(cave: str) -> bool:
    return cave.lower() == cave


def check_cave_visits(path: Tuple[str, ...], next_cave: str) -> bool:
    if is_small(next_cave):
        if path.count(next_cave) == 0:
            return True
        if path.count(next_cave) == 2:
            # Already visited this small cave twice
            return False
        else:
            # Check if any other small caves was visited twice
            counts = Counter(path)
            for cave, count in counts.items():
                if is_small(cave) and count == 2:
                    return False
            else:
                return True
    else:
        return True


def find_paths(
    mapping: DefaultDict[str, Set[str]], paths: Set[Tuple[str, ...]]
) -> Set[Tuple[str, ...]]:
    new_paths: Set[Tuple[str, ...]] = set()
    for path in paths:
        if path[-1] != "end":
            # This path is not complete, look at the neighbors
            # of the last cave in it
            next_caves = mapping[path[-1]]
            for next_cave in next_caves:
                if next_cave == "start":
                    continue
                elif is_small(next_cave):
                    if next_cave not in path:
                        # small cave that was not visited
                        new_path = (*path, next_cave)
                        new_paths.add(new_path)
                    else:
                        # small cave that was visited
                        # we can only visit it again if we
                        # haven't visited any other small cave
                        # twice
                        if check_cave_visits(path, next_cave):
                            new_path = (*path, next_cave)
                            new_paths.add(new_path)
                else:
                    # Big cave, we can visit it multiple times
                    new_path = (*path, next_cave)
                    new_paths.add(new_path)
        else:
            # Already complete path
            new_paths.add(path)

    return new_paths


def compute(mapping: DefaultDict[str, Set[str]]) -> List[List[str]]:
    paths: Set[List[str]] = {("start",)}
    done = False
    while not done:
        done = True
        paths = find_paths(mapping, paths)
        for path in paths:
            if path[-1] != "end":
                done = False

    return paths


def main() -> int:
    with open(os.path.join("day12", "input.txt"), "r") as f_in:
        input_s = f_in.read()
    mapping = parse(input_s)
    paths = compute(mapping)
    print(len(paths))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
