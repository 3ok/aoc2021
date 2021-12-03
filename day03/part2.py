import os
from typing import List
from collections import Counter
from copy import copy


def compute(binaries: List[str]) -> int:
    oxygen_binaries = binaries.copy()
    co2_binaries = binaries.copy()
    length = len(binaries[0])  # 12

    for pos in range(length):
        bits = [b[pos] for b in oxygen_binaries]
        count = Counter(bits).most_common()
        most_common_bit, most_common_occurences = count[0]
        least_common_bit, least_common_occurences = count[1]

        if most_common_occurences > least_common_occurences:
            oxygen_binaries = [b for b in oxygen_binaries if b[pos] == most_common_bit]
        else:
            oxygen_binaries = [b for b in oxygen_binaries if b[pos] == "1"]

        if len(oxygen_binaries) <= 1:
            break
    
    for pos in range(length):
        bits = [b[pos] for b in co2_binaries]
        count = Counter(bits).most_common()
        most_common_bit, most_common_occurences = count[0]
        least_common_bit, least_common_occurences = count[1]

        if most_common_occurences > least_common_occurences:
            co2_binaries = [b for b in co2_binaries if b[pos] == least_common_bit]
        else:
            co2_binaries = [b for b in co2_binaries if b[pos] == "0"]

        if len(co2_binaries) <= 1:
            break
    
    if len(co2_binaries) == 1 and len(oxygen_binaries) == 1:
        return int(co2_binaries[0], 2) * int(oxygen_binaries[0], 2)
    else:
        raise ValueError("Found no or multiple binaries respecting the filter")


def parse(input_s: str) -> List[str]:
    return input_s.split()


def main() -> int:
    with open(os.path.join("day03", "input2.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    
    result = compute(parse(input_s))
    print(result)
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())