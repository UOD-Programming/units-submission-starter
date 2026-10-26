import os
import sys
from io import StringIO
from unittest.mock import patch
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_07.src.exercises.Exercise_05 import load_grid, max_num_in_rows, max_num_adv


def test_load_grid_5_by_5():
    # Define mock file content
    mock_file_content = (
        "83689\n"
        "84451\n"
        "91232\n"
        "27567\n"
        "77133\n"
    )

    # Mock the open function to return a StringIO object
    with patch("builtins.open", return_value=StringIO(mock_file_content)):
        grid = load_grid(UNIT_ROOT / "src/exercises/Exercise_05_grid_5_by_5.txt")
        expected = [
            [8, 3, 6, 8, 9],
            [8, 4, 4, 5, 1],
            [9, 1, 2, 3, 2],
            [2, 7, 5, 6, 7],
            [7, 7, 1, 3, 3],
        ]
        assert grid == expected, f"Loaded grid did not match expected. Got {grid}"


def test_max_num_adv_3_by_3():
    with patch("unit_07.src.exercises.Exercise_05.load_grid", return_value=[[9, 5, 4], [2, 1, 3], [6, 8, 7]]):
        grid = load_grid(UNIT_ROOT / "src/exercises/Exercise_05_grid_3_by_3.txt")
        assert max_num_adv(grid, 2) == 95
        assert max_num_adv(grid, 3) == 954


def test_max_num_in_rows_3_by_3():
    with patch("unit_07.src.exercises.Exercise_05.load_grid", return_value=[[9, 5, 4], [2, 1, 3], [6, 8, 7]]):
        grid = load_grid(UNIT_ROOT / "src/exercises/Exercise_05_grid_3_by_3.txt")
        assert max_num_in_rows(grid, 2) == 94
        assert max_num_in_rows(grid, 3) == 945


def test_max_num_in_rows_5_by_5():
    with patch("unit_07.src.exercises.Exercise_05.load_grid", return_value=[
        [9, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
    ]):
        grid = load_grid(UNIT_ROOT / "src/exercises/Exercise_05_grid_5_by_5.txt")
        assert max_num_in_rows(grid, 2) == 91
        assert max_num_in_rows(grid, 3) == 912
        assert max_num_in_rows(grid, 4) == 9123


def test_max_num_adv_5_by_5():
    with patch("unit_07.src.exercises.Exercise_05.load_grid", return_value=[
        [9, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
    ]):
        grid = load_grid(UNIT_ROOT / "src/exercises/Exercise_05_grid_5_by_5.txt")
        assert max_num_adv(grid, 2) == 97
        assert max_num_adv(grid, 3) == 971
        assert max_num_adv(grid, 4) == 9127
