
from aocd.models import Puzzle

from core import test_and_submit
from util import Matrix, add_tuples, directions


def solution(input: str) -> tuple[any, any]:
    matrix = Matrix(input)
    starting_pos = None
    for row in range(matrix.row_count):
        for col in range(matrix.col_count):
            if matrix.get_item(row, col) == "^":
                starting_pos = (row, col)
                break


    direction_order = ["up", "right", "down", "left"]
    direction = 0

    visited_positions = set()
    current = starting_pos
    while matrix.get_item_pos(current) is not None:
        visited_positions.add(current)
        next_pos = add_tuples(current, directions[direction_order[direction]])
        if matrix.get_item_pos(next_pos) == "#":
            direction = (direction + 1) % 4
            continue

        current = next_pos

    result = len(visited_positions)
    return (result, None)

puzzle = Puzzle(2024, 6)
test_and_submit(puzzle, solution, False)
