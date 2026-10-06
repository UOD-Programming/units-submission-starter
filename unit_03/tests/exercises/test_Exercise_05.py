import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Importing from utils


def test_grade_0():
    """Tests conversion of grade 0 (F)."""
    stdout, stderr = run_program("Exercise_05.py", ['0'], directory="exercises")
    expected_output = "0 = F."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output"


def test_grade_35():
    """Tests conversion of grade 35 (MF)."""
    stdout, stderr = run_program("Exercise_05.py", ['35'], directory="exercises")
    expected_output = "35 = MF."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output"


def test_grade_50():
    """Tests conversion of grade 50 (C)."""
    stdout, stderr = run_program("Exercise_05.py", ['50'], directory="exercises")
    expected_output = "50 = C."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output"


def test_grade_80():
    """Tests conversion of grade 80 (A)."""
    stdout, stderr = run_program("Exercise_05.py", ['80'], directory="exercises")
    expected_output = "80 = A."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output"


def test_grade_90():
    """Tests conversion of grade 90 (A+)."""
    stdout, stderr = run_program("Exercise_05.py", ['90'], directory="exercises")
    expected_output = "90 = A+."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output"


def test_invalid_input_neg1():
    """Tests invalid input -1 followed by valid input 50."""
    stdout, stderr = run_program("Exercise_05.py", ['-1', '50'], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"
    assert "ERROR: input not between 0 and 100" in stdout, "Error message not found for invalid input"
    assert "50 = C." in stdout, "Expected output for valid input '50' not found"


def test_invalid_input_200():
    """Tests invalid input 200 followed by valid input 60."""
    stdout, stderr = run_program("Exercise_05.py", ['200', '60'], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"
    assert "ERROR: input not between 0 and 100" in stdout, "Error message not found for invalid input"
    assert "60 = B." in stdout, "Expected output for valid input '60' not found"


def test_input_prompt():
    """Tests that the input prompt is correctly displayed."""
    stdout, _ = run_program("Exercise_05.py", ["50"], directory="exercises")
    assert "Please enter the grade you wish to convert (0-100)." in stdout, \
        "Input prompt is missing or incorrect"
