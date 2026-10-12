import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def get_final_output(output):
    """Extracts the final line from the program's output."""
    lines = output.split('\n')
    return lines[-1] if lines else ""


def test_average_of_three_numbers():
    """Tests the average calculation for input numbers 3, 6.1, 0."""
    inputs = ["3", "6.1", "0"]
    expected_output = "The average of the numbers entered is 4.55"
    full_output, _ = run_program("Exercise_01.py", inputs, directory="exercises")
    final_output = get_final_output(full_output)
    assert final_output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{final_output}"


def test_no_numbers_entered():
    """Tests the case when only 0 is entered, meaning no numbers were entered."""
    inputs = ["0"]
    expected_output = "No numbers entered."
    full_output, _ = run_program("Exercise_01.py", inputs, directory="exercises")
    final_output = get_final_output(full_output)
    assert final_output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{final_output}"


def test_average_of_multiple_numbers():
    """Tests the average calculation for input numbers 1, 2, 3, 0."""
    inputs = ["1", "2", "3", "0"]
    expected_output = "The average of the numbers entered is 2.0"
    full_output, _ = run_program("Exercise_01.py", inputs, directory="exercises")
    final_output = get_final_output(full_output)
    assert final_output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{final_output}"
