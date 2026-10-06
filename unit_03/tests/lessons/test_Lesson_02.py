import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Import from utils


def test_divisible_by_3_and_5():
    """Tests if the program correctly identifies a number divisible by both 3 and 5."""
    stdout, stderr = run_program("Lesson_02.py", ["15"], directory="lessons")
    expected_output = "Your number is divisible by 3 and 5."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 15, but got '{stdout}'"


def test_divisible_by_3_not_5():
    """Tests if the program correctly identifies a number divisible by 3 but not 5."""
    stdout, stderr = run_program("Lesson_02.py", ["12"], directory="lessons")
    expected_output = "Your number is divisible by 3 and NOT by 5."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 12, but got '{stdout}'"


def test_not_divisible_by_3_but_5():
    """Tests if the program correctly identifies a number divisible by 5 but not 3."""
    stdout, stderr = run_program("Lesson_02.py", ["20"], directory="lessons")
    expected_output = "Your number is NOT divisible by 3 and is divisible by 5."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 20, but got '{stdout}'"


def test_not_divisible_by_3_or_5():
    """Tests if the program correctly identifies a number not divisible by 3 or 5."""
    stdout, stderr = run_program("Lesson_02.py", ["16"], directory="lessons")
    expected_output = "Your number is NOT divisible by 3 and 5."
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 16, but got '{stdout}'"


def test_input_prompt():
    """Tests that the input prompt is correctly displayed."""
    stdout, _ = run_program("Lesson_02.py", ["15"], directory="lessons")
    expected_prompt = "Please enter a number:"
    assert expected_prompt in stdout, f"Expected input prompt '{expected_prompt}' not found in output."
