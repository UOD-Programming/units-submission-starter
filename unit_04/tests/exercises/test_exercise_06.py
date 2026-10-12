import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_output(output):
    """Removes all whitespace and converts to lowercase."""
    return ''.join(output.lower().split())


def test_min_max_average_length_case1():
    """Tests the output for a list of strings with varying lengths."""
    inputs = ["one,two,three,four,five"]  # Input string

    expected_outputs = [
        "The minimum length of a string is 3",
        "The maximum length of a string is 5",
        "The average length of the strings in the list is 3.8"
    ]

    stdout, stderr = run_program("Exercise_06.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_min_max_average_length_case2():
    """Tests the output for a list of strings where all strings are of the same length."""
    inputs = ["aaa,bbb,ccc"]  # Input string with uniform length

    expected_outputs = [
        "The minimum length of a string is 3",
        "The maximum length of a string is 3",
        "The average length of the strings in the list is 3.0"
    ]

    stdout, stderr = run_program("Exercise_06.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_min_max_average_length_case3():
    """Tests the output for a list of strings with a single string."""
    inputs = ["hello"]  # Single string

    expected_outputs = [
        "The minimum length of a string is 5",
        "The maximum length of a string is 5",
        "The average length of the strings in the list is 5.0"
    ]

    stdout, stderr = run_program("Exercise_06.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"
