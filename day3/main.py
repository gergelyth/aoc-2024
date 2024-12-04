import re

from aocd.models import Puzzle

from core import test_and_submit


def solution(input: str) -> tuple[any, any]:
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    mul_matches = {match.start(): match for match in re.finditer(mul_pattern, input)}
    do_matches = {match.start(): match for match in re.finditer(do_pattern, input)}
    dont_matches = {match.start(): match for match in re.finditer(dont_pattern, input)}

    all_keys = sorted(list(mul_matches.keys()) + list(do_matches.keys()) + list(dont_matches.keys()))

    result = 0
    mul_enabled = True
    for i in all_keys:
        if i in do_matches:
            mul_enabled = True
            continue

        if i in dont_matches:
            mul_enabled = False
            continue

        if mul_enabled:
            mul_match = mul_matches[i]
            result += int(mul_match.group(1)) * int(mul_match.group(2))

    return (None, result)

puzzle = Puzzle(2024, 3)
test_and_submit(puzzle, solution, False)
