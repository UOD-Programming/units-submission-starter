import timeit
from unittest.mock import patch
import pytest
import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_08.src.exercises.Exercise_03 import find_best_path


def test_find_best_path_correctness():
    test_cases = [
        {
            "grid": {
                "size": (99, 99),
                (1, 0): 1, (1, 1): 3, (1, 2): 2, (1, 5): 3,
                (2, 0): 2, (2, 1): 3, (2, 2): 2, (2, 3): 1,
                (3, 1): 3, (3, 5): 2,
                (4, 1): 3, (4, 3): 2,
                (97, 98): 1, (98, 98): 3
            },
            "expected_result": 19
        },
        {
            "grid": {
                "size": (5, 6),
                (1, 0): 1,
                (1, 1): 3,
                (1, 2): 2,
                (1, 5): 3,
                (2, 0): 2,
                (2, 1): 3,
                (2, 2): 2,
                (2, 3): 1,
                (3, 1): 3,
                (3, 5): 2,
                (4, 1): 3,
                (4, 3): 2
            },
            "expected_result": 15
        }
    ]

    for case in test_cases:
        grid = case["grid"]
        expected_result = case["expected_result"]

        try:
            result = find_best_path(grid)
        except Exception as e:
            pytest.fail(f"Main method failed. {e}")

        assert result == expected_result


def test_find_best_path_time():
    test_find_best_path_correctness()
    test_cases = [
        {
            "grid": {
                "size": (99, 99),
                (1, 0): 1, (1, 1): 3, (1, 2): 2, (1, 5): 3,
                (2, 0): 2, (2, 1): 3, (2, 2): 2, (2, 3): 1,
                (3, 1): 3, (3, 5): 2,
                (4, 1): 3, (4, 3): 2,
                (97, 98): 1, (98, 98): 3
            }
        },
        {
            "grid": {
                "size": (5, 6),
                (1, 0): 1,
                (1, 1): 3,
                (1, 2): 2,
                (1, 5): 3,
                (2, 0): 2,
                (2, 1): 3,
                (2, 2): 2,
                (2, 3): 1,
                (3, 1): 3,
                (3, 5): 2,
                (4, 1): 3,
                (4, 3): 2
            }
        }
    ]

    for case in test_cases:
        grid = case["grid"]

        start_time = timeit.default_timer()
        try:
            find_best_path(grid)
        except Exception as e:
            pytest.fail(f"Main method failed during timing test. {e}")
        end_time = timeit.default_timer()

        time_taken = end_time - start_time
        assert time_taken < 1, f"Execution time exceeded: {time_taken} seconds"
