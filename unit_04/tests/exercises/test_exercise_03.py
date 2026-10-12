import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_output(output):
    """Removes all whitespace and converts to lowercase."""
    return ''.join(output.lower().split())


def test_largest_of_multiple_numbers():
    """Tests for a set of positive numbers."""
    inputs = [3, 10, 32, -1, 0]
    expected_output = "The largest of the numbers entered is 32"
    
    stdout, stderr = run_program("Exercise_03.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"Expected: {expected_output}\nGot: {stdout.strip()}"


def test_largest_of_negative_numbers():
    """Tests for a set of negative numbers."""
    inputs = [-5, -10, -3, -1, 0]
    expected_output = "The largest of the numbers entered is -1"
    
    stdout, stderr = run_program("Exercise_03.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"Expected: {expected_output}\nGot: {stdout.strip()}"


def test_no_numbers_entered():
    """Tests the case when no valid numbers were entered (just 0)."""
    inputs = [0]
    expected_output = "No numbers entered."
    
    stdout, stderr = run_program("Exercise_03.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"Expected: {expected_output}\nGot: {stdout.strip()}"


def test_largest_with_zero():
    """Tests for a set of positive numbers including 0."""
    inputs = [100, 50, 75, 0]
    expected_output = "The largest of the numbers entered is 100"
    
    stdout, stderr = run_program("Exercise_03.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)

    assert normalized_expected in normalized_output, f"Expected: {expected_output}\nGot: {stdout.strip()}"

