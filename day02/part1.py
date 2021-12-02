from typing import Generator, Tuple, TypedDict
from enum import Enum
import os

class Position(TypedDict):
    horizontal: int
    depth: int

class Instruction(Enum):
    FORWARD = 0
    DOWN = 1
    UP = -1
    
    
def parse(input_s: str) -> Generator[Tuple[Instruction, int], None, None]:
    for line in input_s.split("\n"):
        instruction_str, number_str = line.split()
    
        number = int(number_str)
        if instruction_str == "forward":
            instruction = Instruction.FORWARD
        elif instruction_str == "down":
            instruction = Instruction.DOWN
        else:
            instruction = Instruction.UP
        
        yield instruction, number

def compute(position: Position, gen: Generator[Tuple[Instruction, int], None, None]) -> int:
    for instruction, number in gen:
        if instruction == Instruction.FORWARD:
            position["horizontal"] += number
        elif instruction == Instruction.DOWN:
            position["depth"] += number
        else:
            position["depth"] -= number
    
    return position["depth"] * position["horizontal"]


def main() -> int:
    with open(os.path.join("day02", "input1.txt"), "r") as f_in:
        input_s = f_in.read().strip()
    
    position: Position = {"horizontal": 0, "depth": 0}
    result = compute(position, parse(input_s))
    print(result)
    
    return 0