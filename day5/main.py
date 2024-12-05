
from aocd.models import Puzzle

from core import test_and_submit
from util import get_lines


def get_correct_update(pages: list[str], rules: dict[str, set[str]]) -> list[str]:
    all_pages = set(pages)
    previous_pages = set()
    correct_order = []
    for page in pages:
        if page in previous_pages:
            continue

        if page in rules:
            must_be_before_pages = all_pages.intersection(rules[page])
            wrong_order_pages = [p for p in must_be_before_pages if p not in previous_pages]
            if wrong_order_pages:
                previous_pages.update(wrong_order_pages)
                correct_order += wrong_order_pages

        previous_pages.add(page)
        correct_order.append(page)

    return correct_order

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
        corrected = False

        updated = parts
        while True:
            new_updated = get_correct_update(updated, rules)
            if new_updated == updated:
                break
            corrected = True
            updated = new_updated

        if corrected:
            middle = updated[len(updated)//2]
            result += int(middle)

    return (None, result)

puzzle = Puzzle(2024, 5)
test_and_submit(puzzle, solution, False)
