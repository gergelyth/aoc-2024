from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)
    result = 0
    for line in lines:
        numbers = [int(x) for x in line.split()]
        first_diff = numbers[1] - numbers[0]
        is_safe = all([first_diff * (y-x) > 0 and 1 <= abs(y-x) <= 3 for (x,y) in zip(numbers, numbers[1:])])
        if is_safe:
            result +=1

    return (result, False)

puzzle = Puzzle(2024, 2)
test_and_submit(puzzle, solution, False)
