import os
import sys
import random
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_07.src.lessons.Lesson_03 import number_of_lines


def test_number_of_lines_test_txt():
    filename = UNIT_ROOT / "src/lessons/Lesson_03_test.txt"
    expected_lines = 25
    assert number_of_lines(filename) == expected_lines, f"Failed to count lines in {filename}"


def test_number_of_lines_example_txt():
    filename = UNIT_ROOT / "src/lessons/Lesson_03_example.txt"
    expected_lines = 9
    assert number_of_lines(filename) == expected_lines, f"Failed to count lines in {filename}"


def test_number_of_lines_random_file(tmp_path):
    # Setup: Create a random file with a random number of lines
    filename = tmp_path / "random_test.txt"
    random_lines = random.randint(1, 100)
    try:
        with open(filename, 'w') as f:
            for _ in range(random_lines):
                f.write("This is a test line.\n")

        # Test: Check the number of lines in the file
        assert number_of_lines(filename) == random_lines, f"Failed to count lines in {filename}. Expected {random_lines}"
    finally:
        # Teardown: Remove the test file
        if os.path.exists(filename):
            os.remove(filename)
