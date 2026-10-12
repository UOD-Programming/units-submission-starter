import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_output(output):
    """Splits the output into lines, removes any empty lines, and strips each line."""
    return '\n'.join(line.strip() for line in output.split('\n') if line.strip())


def test_triangle_size_3():
    """Tests the output for a triangle of size 3."""
    size = 3
    expected_output = "*\n**\n***"

    stdout, stderr = run_program("Exercise_04.py", [size], directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"For size {size}:\nExpected:\n{normalized_expected}\n\nGot:\n{normalized_output}"


def test_triangle_size_5():
    """Tests the output for a triangle of size 5."""
    size = 5
    expected_output = "*\n**\n***\n****\n*****"

    stdout, stderr = run_program("Exercise_04.py", [size], directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"For size {size}:\nExpected:\n{normalized_expected}\n\nGot:\n{normalized_output}"


def test_triangle_size_1():
    """Tests the output for a triangle of size 1."""
    size = 1
    expected_output = "*"

    stdout, stderr = run_program("Exercise_04.py", [size], directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"For size {size}:\nExpected:\n{normalized_expected}\n\nGot:\n{normalized_output}"


def test_triangle_size_6():
    """Tests the output for a triangle of size 6."""
    size = 6
    expected_output = "*\n**\n***\n****\n*****\n******"

    stdout, stderr = run_program("Exercise_04.py", [size], directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"For size {size}:\nExpected:\n{normalized_expected}\n\nGot:\n{normalized_output}"

