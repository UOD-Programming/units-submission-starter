import os
import sys

# Add the path to the "Exercise_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_06.src.exercises.Exercise_01 import find_max_row


def test_find_max_row_case1():
    grid = [[1, 2, 3], [4, 2, 1], [4, 5, 4]]
    expected_output = 3
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case2():
    grid = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case3():
    grid = [[1, 2, 3], [3], [2, 1, 3, 4]]
    expected_output = 3
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case4():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case5():
    grid = [[10], [5, 5], [3, 3, 3], [2, 2, 2, 2]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case6():
    grid = [[-1, -2, -3], [-4, -5, -6]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case7():
    grid = [[0]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"


def test_find_max_row_case8():
    grid = [[1, 2], [2, 1], [1, 1, 1]]
    expected_output = 1
    assert find_max_row(grid) == expected_output, f"For grid {grid}: Expected {expected_output}, but got {find_max_row(grid)}"

