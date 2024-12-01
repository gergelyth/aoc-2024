from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)
    col1 = []
    col2 = []
    col2_counts = {}

    for line in lines:
        parts = line.split()
        col1.append(int(parts[0]))

        number = int(parts[1])
        col2.append(number)
        col2_counts[number] = col2_counts.get(number, 0) + 1

    result = sum([col2_counts.get(i, 0) * i for i in col1])
    return (None, result)

puzzle = Puzzle(2024, 1)
test_and_submit(puzzle, solution, False)
