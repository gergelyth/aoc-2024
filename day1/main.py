from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)
    return (sum, sum)

puzzle = Puzzle(2024, 1)
test_and_submit(puzzle, solution, True)
