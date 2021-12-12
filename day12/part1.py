from typing import List, Set, Tuple
from typing import DefaultDict
from collections import defaultdict
import os


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


def find_paths(
    mapping: DefaultDict[str, Set[str]], paths: List[List[str]]
) -> List[List[str]]:
    new_paths: List[List[str]] = []
    for path in paths:
        if path[-1] != "end":
            # This path is not complete, look at the neighbors
            # of the last cave in it
            next_caves = mapping[path[-1]]
            for next_cave in next_caves:
                if is_small(next_cave):
                    if next_cave not in path:
                        # small cave that was not visited
                        new_path = path.copy()
                        new_path.append(next_cave)
                        if new_path not in new_paths:
                            new_paths.append(new_path)
                else:
                    # Big cave, we can visit it multiple times
                    new_path = path.copy()
                    new_path.append(next_cave)
                    if new_path not in new_paths:
                        new_paths.append(new_path)
        else:
            # Already complete path
            if path not in new_paths:
                new_paths.append(path)

    return new_paths


def compute(mapping: DefaultDict[str, Set[str]]) -> List[List[str]]:
    paths: List[List[str]] = [["start"] for _ in mapping["start"]]
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
