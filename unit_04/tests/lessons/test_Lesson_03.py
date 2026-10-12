import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_line(line):
    """Trims leading and trailing whitespace but preserves the core content."""
    return line.strip()


def compare_output_line_by_line(actual, expected):
    """Compares two outputs line by line, providing student-friendly feedback."""
    actual_lines = actual.strip().split('\n')
    expected_lines = expected.strip().split('\n')

    assert len(actual_lines) == len(expected_lines), (
        f"Number of lines in the output doesn't match.\n"
        f"Expected {len(expected_lines)} lines but got {len(actual_lines)}.\n"
        f"Expected:\n{expected}\n\nGot:\n{actual}"
    )

    for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines)):
        assert normalize_line(actual_line) == normalize_line(expected_line), (
            f"Line {i + 1} does not match.\n"
            f"Expected: {expected_line}\n"
            f"Got: {actual_line}"
        )


def test_string_length_case1():
    """Tests the string length output for a list of car brands with relaxed formatting checks."""
    # Input string simulating user input
    user_input = "Citreon,Ford,Audi,Mercedes"

    # Expected output from the script
    expected_output = (
        "Please enter a list of numbers separated by a comma.\n"
        "e.g. Citreon,Ford,Audi,Mercedes\n"
        "The length of the string Citreon is 7.\n"
        "The length of the string Ford is 4.\n"
        "The length of the string Audi is 4.\n"
        "The length of the string Mercedes is 8."
    )

    # Run the program
    stdout, stderr = run_program("Lesson_03.py", [user_input], directory="lessons")

    # Ensure there are no errors
    assert stderr.strip() == "", "The program should not produce any errors"

    # Compare the output line-by-line
    compare_output_line_by_line(stdout, expected_output)


def test_string_length_case2():
    """Tests the string length output for a different list of car brands with relaxed formatting checks."""
    # Input string simulating user input
    user_input = "BMW,Ferrari,Toyota"

    # Expected output from the script
    expected_output = (
        "Please enter a list of numbers separated by a comma.\n"
        "e.g. Citreon,Ford,Audi,Mercedes\n"
        "The length of the string BMW is 3.\n"
        "The length of the string Ferrari is 7.\n"
        "The length of the string Toyota is 6."
    )

    # Run the program
    stdout, stderr = run_program("Lesson_03.py", [user_input], directory="lessons")

    # Ensure there are no errors
    assert stderr.strip() == "", "The program should not produce any errors"

    # Compare the output line-by-line
    compare_output_line_by_line(stdout, expected_output)

