
from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def is_correct_update(pages: list[str], rules: dict[str, set[str]]) -> bool:
    all_pages = set(pages)
    previous_pages = set()
    for page in pages:
        if page in rules:
            must_be_before_pages = all_pages.intersection(rules[page])
            if any(p not in previous_pages for p in must_be_before_pages):
                return False

        previous_pages.add(page)

    return True

def solution(input: str) -> tuple[any, any]:
    lines = get_lines(input)

    rules = {}
    for i, line in enumerate(lines):
        if line == "":
            updates = lines[i+1:]
            break

        page_before, page = line.split("|")
        if page not in rules:
            rules[page] = set()
        rules[page].add(page_before)

    result = 0
    for update in updates:
        parts = update.split(",")
        if is_correct_update(parts, rules):
            middle = parts[len(parts)//2]
            result += int(middle)

    return (result, None)

puzzle = Puzzle(2024, 5)
test_and_submit(puzzle, solution, False)
