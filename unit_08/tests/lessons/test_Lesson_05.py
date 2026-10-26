import pytest
import timeit
import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_05 import no_paths_memo  # Assuming the file is named path_finding.py

def test_values():
    assert no_paths_memo(12, 12, {}) == 2704156
    assert no_paths_memo(10, 10, {}) == 184756
    assert no_paths_memo(6, 6, {}) == 924

def test_performance():
    assert no_paths_memo(12, 12, {}) == 2704156
    assert no_paths_memo(10, 10, {}) == 184756
    assert no_paths_memo(6, 6, {}) == 924
    start_time = timeit.default_timer()
    no_paths_memo(99, 99, {})
    end_time = timeit.default_timer()

    time_taken = end_time - start_time

    assert time_taken < 1, f"Time taken ({time_taken} seconds) exceeds 1 second limit"