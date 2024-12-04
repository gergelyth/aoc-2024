
from aocd.models import Puzzle

from core import test_and_submit
from util import Matrix

TARGET = "MAS"
BACKWARDS = "SAM"

def is_target(matrix: Matrix, positions: list[tuple[int, int]]) -> bool:
    constructed_word = ""
    for position in positions:
        constructed_word += matrix.get_item_pos(position) or ""

    return constructed_word in (TARGET, BACKWARDS)

def solution(input: str) -> tuple[any, any]:
    matrix = Matrix(input)

    result = 0
    for row in range(matrix.row_count):
        for col in range(matrix.col_count):
            going_right = is_target(matrix, [(row+i, col+i) for i in range(3)])
            going_left = is_target(matrix, [(row+i, col+2-i) for i in range(3)])

            if going_right and going_left:
                result += 1

    return (None, result)

puzzle = Puzzle(2024, 4)
test_and_submit(puzzle, solution, False)
