from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)
    col1 = []
    col2 = []
    for line in lines:
        parts = line.split()
        col1.append(int(parts[0]))
        col2.append(int(parts[1]))

    col1.sort()
    col2.sort()

    differences = [abs(x - y) for x, y in zip(col1, col2)]
    return (sum(differences), None)

puzzle = Puzzle(2024, 1)
test_and_submit(puzzle, solution, True)
