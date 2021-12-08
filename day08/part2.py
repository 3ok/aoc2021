from collections import defaultdict
import os
from typing import Counter, DefaultDict, Dict, List, Set, Tuple

UNIQUE_NUMBERS = {
    2: "1",
    3: "7",
    4: "4",
    7: "8",
}

DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def find_partial_mapping_from_unique_numbers(digits: List[str]) -> Dict[str, Set[str]]:
    segments_mapping: DefaultDict[str, Set[str]] = defaultdict(set)
    appears_in: DefaultDict[str, Set[str]] = defaultdict(set)
    for digit in digits:
        n_segments = len(digit)
        if n_segments in UNIQUE_NUMBERS:
            num = UNIQUE_NUMBERS[n_segments]
            for segment in digit:
                appears_in[segment].add(num)

    for segment, nums in appears_in.items():
        if nums == {"1", "4", "7", "8"}:
            segments_mapping["c"].add(segment)
            segments_mapping["f"].add(segment)
        elif nums == {"4", "8"}:
            segments_mapping["b"].add(segment)
            segments_mapping["d"].add(segment)
        elif nums == {"7", "8"}:
            segments_mapping["a"].add(segment)
        elif nums == {"8"}:
            segments_mapping["e"].add(segment)
            segments_mapping["g"].add(segment)
        else:
            raise ValueError("Something is wrong !")
    return segments_mapping


def find_partial_mapping_from_counts(digits: List[str]) -> Dict[str, Set[str]]:
    segments_mapping: DefaultDict[str, Set[str]] = defaultdict(set)

    segments_count = Counter("".join(digits))
    for segment, count in segments_count.items():
        if count == 8:
            segments_mapping["a"].add(segment)
            segments_mapping["c"].add(segment)
        elif count == 7:
            segments_mapping["d"].add(segment)
            segments_mapping["g"].add(segment)
        elif count == 6:
            segments_mapping["b"].add(segment)
        elif count == 4:
            segments_mapping["e"].add(segment)
        elif count == 9:
            segments_mapping["f"].add(segment)
        else:
            raise ValueError("Something is wrong !")

    return segments_mapping


def find_mapping(digits: List[str]) -> Dict[str, str]:
    segments_mapping_counts = find_partial_mapping_from_counts(digits)
    segments_mapping_unique_numbers = find_partial_mapping_from_unique_numbers(digits)

    segments_mapping: Dict[str, str] = {}
    for segment in "abcdefg":
        candidate = segments_mapping_counts[segment].intersection(
            segments_mapping_unique_numbers[segment]
        )
        if len(candidate) == 1:
            segments_mapping[segment] = candidate.pop()
        else:
            raise ValueError("Something is wrong !")

    return segments_mapping


def decode(digit: str, segments_mapping: Dict[str, str]) -> int:
    decoded_digit = digit.translate(
        {ord(v): ord(k) for k, v in segments_mapping.items()}
    )

    return DIGITS["".join(sorted(decoded_digit))]


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    first, second = line.split(" | ")
    first_digits = first.split()
    second_digits = second.split()
    return first_digits, second_digits


def parse(input_s: str) -> List[Tuple[List[str], List[str]]]:
    return [parse_line(line) for line in input_s.split("\n")]


def main() -> int:
    with open(os.path.join("day08", "input.txt"), "r") as f_in:
        input_s = f_in.read()

    all_digits = parse(input_s)
    result = 0
    for digits, digits_to_decode in all_digits:
        segments_mapping = find_mapping(digits)
        line_result = 0
        for digit_to_decode in digits_to_decode:
            line_result = decode(digit_to_decode, segments_mapping) + 10 * line_result
        result += line_result
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
