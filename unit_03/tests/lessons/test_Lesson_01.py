import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Importing from utils


def test_even_number():
    """Tests if the program correctly identifies an even number."""
    stdout, stderr = run_program("Lesson_01.py", ["4"], directory="lessons")
    expected_output = "Your number is even!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}', but got '{stdout}'"


def test_odd_number():
    """Tests if the program correctly identifies an odd number."""
    stdout, stderr = run_program("Lesson_01.py", ["7"], directory="lessons")
    expected_output = "Your number is odd!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}', but got '{stdout}'"


def test_zero():
    """Tests if the program handles zero correctly."""
    stdout, stderr = run_program("Lesson_01.py", ["0"], directory="lessons")
    expected_output = "Your number is even!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input 0, but got '{stdout}'"


def test_negative_even_number():
    """Tests if the program correctly identifies a negative even number."""
    stdout, stderr = run_program("Lesson_01.py", ["-8"], directory="lessons")
    expected_output = "Your number is even!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input -8, but got '{stdout}'"


def test_negative_odd_number():
    """Tests if the program correctly identifies a negative odd number."""
    stdout, stderr = run_program("Lesson_01.py", ["-5"], directory="lessons")
    expected_output = "Your number is odd!"
    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' for input -5, but got '{stdout}'"


def test_input_prompt():
    """Tests that the input prompt is correctly displayed."""
    stdout, _ = run_program("Lesson_01.py", ["4"], directory="lessons")
    expected_prompt = "Please enter a whole number:"
    assert expected_prompt in stdout, f"Expected input prompt '{expected_prompt}' not found in output."
