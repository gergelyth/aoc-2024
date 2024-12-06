
from collections import defaultdict

from aocd.models import Puzzle

from core import test_and_submit
from util import Matrix, add_tuples, directions


def is_loop(matrix: Matrix, starting_pos: tuple[int,int]) -> bool:
    direction_order = ["up", "right", "down", "left"]
    direction = 0

    visited_positions = defaultdict(set)
    current = starting_pos
    while matrix.get_item_pos(current) is not None:
        if current in visited_positions and direction in visited_positions[current]:
            return True

        if current != starting_pos:
            visited_positions[current].add(direction)

        next_pos = add_tuples(current, directions[direction_order[direction]])
        if matrix.get_item_pos(next_pos) == "#":
            direction = (direction + 1) % 4
            continue

        current = next_pos

    return False

def solution(input: str) -> tuple[any, any]:
    matrix = Matrix(input)
    starting_pos = None
    for row in range(matrix.row_count):
        for col in range(matrix.col_count):
            if matrix.get_item(row, col) == "^":
                starting_pos = (row, col)
                break

    result = 0
    for row in range(matrix.row_count):
        for col in range(matrix.col_count):
            if matrix.get_item(row, col) == ".":
                matrix.set_item(row, col, "#")
                print(f"{row * matrix.col_count + col}/{matrix.row_count*matrix.col_count}")
                if is_loop(matrix, starting_pos):
                    result += 1

                matrix.set_item(row, col, ".")

    return (None, result)

puzzle = Puzzle(2024, 6)
test_and_submit(puzzle, solution, False)
