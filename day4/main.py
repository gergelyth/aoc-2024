
from aocd.models import Puzzle

from core import test_and_submit
from util import Matrix

TARGET = "XMAS"
BACKWARDS = "SAMX"

def is_target(matrix: Matrix, positions: list[tuple[int, int]]) -> int:
    constructed_word = ""
    for position in positions:
        constructed_word += matrix.get_item_pos(position) or ""

    return int(constructed_word in (TARGET, BACKWARDS))

def solution(input: str) -> tuple[any, any]:
    matrix = Matrix(input)

    result = 0
    for row in range(matrix.row_count):
        for col in range(matrix.col_count):
            result += is_target(matrix, [(row, col+i) for i in range(4)])
            result += is_target(matrix, [(row+i, col) for i in range(4)])
            result += is_target(matrix, [(row+i, col-i) for i in range(4)])
            result += is_target(matrix, [(row+i, col+i) for i in range(4)])

    return (result, None)

puzzle = Puzzle(2024, 4)
test_and_submit(puzzle, solution, False)
