import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Import from utils


def test_not_raining_and_has_hat():
    """Tests when it is not raining and the user has a hat (no umbrella needed)."""
    stdout, stderr = run_program("Lesson_04.py", [0, 0], directory="lessons")  # is_raining = False, no_hat = False
    expected_output = "False"
    assert not stderr, f"Error occurred: {stderr}"
    assert stdout == expected_output, f"Expected '{expected_output}', but got '{stdout}'"


def test_not_raining_and_no_hat():
    """Tests when it is not raining and the user does not have a hat (no umbrella needed)."""
    stdout, stderr = run_program("Lesson_04.py", [0, 1], directory="lessons")  # is_raining = False, no_hat = True
    expected_output = "False"
    assert not stderr, f"Error occurred: {stderr}"
    assert stdout == expected_output, f"Expected '{expected_output}', but got '{stdout}'"


def test_raining_and_has_hat():
    """Tests when it is raining and the user has a hat (no umbrella needed)."""
    stdout, stderr = run_program("Lesson_04.py", [1, 0], directory="lessons")  # is_raining = True, no_hat = False
    expected_output = "False"
    assert not stderr, f"Error occurred: {stderr}"
    assert stdout == expected_output, f"Expected '{expected_output}', but got '{stdout}'"


def test_raining_and_no_hat():
    """Tests when it is raining and the user does not have a hat (umbrella needed)."""
    stdout, stderr = run_program("Lesson_04.py", [1, 1], directory="lessons")  # is_raining = True, no_hat = True
    expected_output = "True"
    assert not stderr, f"Error occurred: {stderr}"
    assert stdout == expected_output, f"Expected '{expected_output}', but got '{stdout}'"
