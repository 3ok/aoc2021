from typing import List
from collections import Counter
import os


def compute(binaries: List[str]) -> int:
    gamma = ""
    epsilon = ""
    length = len(binaries[0])
    for pos in range(length):
        bits = [b[pos] for b in binaries]
        count = Counter(bits).most_common()
        most_common_bit, _ = count[0]
        least_common_bit, _ = count[1]
        
        gamma += most_common_bit
        epsilon += least_common_bit
        
    return int(gamma, 2) * int(epsilon, 2)


def parse(input_s: str) -> List[str]:
    return input_s.split()


def main() -> int:
    with open(os.path.join("day03", "input1.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    
    result = compute(parse(input_s))
    print(result)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())