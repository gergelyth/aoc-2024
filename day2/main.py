from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def is_valid_sequence(nums):
    first_diff = nums[1] - nums[0]
    return all(first_diff * (y-x) > 0 and 1 <= abs(y-x) <= 3 for x, y in zip(nums, nums[1:]))

def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)
    result = 0
    for line in lines:
        numbers = [int(x) for x in line.split()]
        # terrible complexity
        is_safe = is_valid_sequence(numbers) or any(
            is_valid_sequence(numbers[:i] + numbers[i+1:])
            for i in range(len(numbers))
        )
        if is_safe:
            result += 1

    return (None, result)

puzzle = Puzzle(2024, 2)
test_and_submit(puzzle, solution, False)
