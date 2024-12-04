import re

from aocd.models import Puzzle

from core import test_and_submit


def solution(input: str) -> tuple[any, any]:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, input)

    result = 0
    for (num1, num2) in matches:
        result += int(num1) * int(num2)

    return (result, None)

puzzle = Puzzle(2024, 3)
test_and_submit(puzzle, solution, False)
