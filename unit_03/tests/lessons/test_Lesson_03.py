import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Import from utils


def test_positive_number():
    """Tests if the program correctly identifies a positive number."""
    stdout, stderr = run_program("Lesson_03.py", ["2.3"], directory="lessons")
    expected_output = "Your number is positive!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 2.3, but got '{stdout}'"


def test_negative_number():
    """Tests if the program correctly identifies a negative number."""
    stdout, stderr = run_program("Lesson_03.py", ["-3.3"], directory="lessons")
    expected_output = "Your number is negative!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input -3.3, but got '{stdout}'"


def test_zero():
    """Tests if the program correctly identifies zero."""
    stdout, stderr = run_program("Lesson_03.py", ["0"], directory="lessons")
    expected_output = "Your number is zero!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 0, but got '{stdout}'"


def test_negative_integer():
    """Tests if the program correctly identifies a negative integer."""
    stdout, stderr = run_program("Lesson_03.py", ["-10"], directory="lessons")
    expected_output = "Your number is negative!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input -10, but got '{stdout}'"


def test_positive_integer():
    """Tests if the program correctly identifies a positive integer."""
    stdout, stderr = run_program("Lesson_03.py", ["10"], directory="lessons")
    expected_output = "Your number is positive!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 10, but got '{stdout}'"


def test_input_prompt():
    """Tests that the input prompt is correctly displayed."""
    stdout, _ = run_program("Lesson_03.py", ["0"], directory="lessons")
    expected_prompt = "Please enter a number:"
    assert expected_prompt in stdout, f"Expected input prompt '{expected_prompt}' not found in output."
