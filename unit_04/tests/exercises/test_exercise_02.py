import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_output(output):
    """Removes extra blank lines and trims whitespace from each line."""
    lines = [line.strip() for line in output.strip().split('\n') if line.strip()]
    return '\n'.join(lines)


def test_single_hour_travel():
    """Tests if the output is correct for speed 50 mph and 1 hour."""
    user_input = ["50", "1"]  # Speed: 50 mph, Hours: 1
    
    stdout, stderr = run_program("Exercise_02.py", user_input, directory="exercises")
    
    assert not stderr.strip(), "Exercise_02.py should not produce any errors"
    
    expected_output = (
        "What is the speed of the vehicle in mph?\n"
        "How many hours has it travelled?\n"
        "Hour | Distance Travelled\n"
        "-----------------------\n"
        "1    | 50"
    )
    
    # Normalize both actual and expected output
    normalized_stdout = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)
    
    assert normalized_stdout == normalized_expected, f"Expected:\n{normalized_expected}\n\nGot:\n{normalized_stdout}"


def test_five_hour_travel():
    """Tests if the output is correct for speed 60 mph and 5 hours."""
    user_input = ["60", "5"]  # Speed: 60 mph, Hours: 5
    
    stdout, stderr = run_program("Exercise_02.py", user_input, directory="exercises")
    
    assert not stderr.strip(), "Exercise_02.py should not produce any errors"
    
    expected_output = (
        "What is the speed of the vehicle in mph?\n"
        "How many hours has it travelled?\n"
        "Hour | Distance Travelled\n"
        "-----------------------\n"
        "1    | 60\n"
        "2    | 120\n"
        "3    | 180\n"
        "4    | 240\n"
        "5    | 300"
    )
    
    # Normalize both actual and expected output
    normalized_stdout = normalize_output(stdout)
    normalized_expected = normalize_output(expected_output)
    
    assert normalized_stdout == normalized_expected, f"Expected:\n{normalized_expected}\n\nGot:\n{normalized_stdout}"


def test_negative_speed():
    """Tests if the output handles invalid input when speed is negative."""
    user_input = ["-10", "2"]  # Invalid Speed: -10 mph, Hours: 2
    
    stdout, stderr = run_program("Exercise_02.py", user_input, directory="exercises")
    
    expected_error_message = "ERROR: Speed must be a positive number."
    
    assert not stderr.strip(), "Exercise_02.py should not produce any errors"
    
    # Normalize stdout
    normalized_stdout = normalize_output(stdout)
    
    assert expected_error_message in normalized_stdout, f"Expected error message not found. Got:\n{normalized_stdout}"


def test_negative_hours():
    """Tests if the output handles invalid input when hours are negative."""
    user_input = ["50", "-3"]  # Speed: 50 mph, Invalid Hours: -3
    
    stdout, stderr = run_program("Exercise_02.py", user_input, directory="exercises")
    
    expected_error_message = "ERROR: Hours travelled must be a positive number."
    
    assert not stderr.strip(), "Exercise_02.py should not produce any errors"
    
    # Normalize stdout
    normalized_stdout = normalize_output(stdout)
    
    assert expected_error_message in normalized_stdout, f"Expected error message not found. Got:\n{normalized_stdout}"
