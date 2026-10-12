import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def test_print_numbers():
    # Run the script using the run_program function from utils
    stdout, stderr = run_program("Lesson_04.py", [], directory="lessons")

    # Ensure there are no errors
    assert stderr.strip() == "", "The program should not produce any errors"

    # Split the output into lines and convert to integers
    try:
        output_numbers = [int(num) for num in stdout.strip().split('\n')]
    except ValueError:
        pytest.fail("The output contains non-integer values")

    # Check if the output has exactly 99 numbers (100 - 1 for the excluded 42)
    assert len(output_numbers) == 99, f"Expected 99 numbers, but got {len(output_numbers)}"

    # Check if the numbers are in the correct range and order
    expected_numbers = list(range(1, 42)) + list(range(43, 101))
    assert output_numbers == expected_numbers, "The output doesn't match the expected sequence"

    # Check if 42 is not in the output
    assert 42 not in output_numbers, "42 should not be in the output"

    # Check if the first number is 1 and the last number is 100
    assert output_numbers[0] == 1, f"The first number should be 1, but got {output_numbers[0]}"
    assert output_numbers[-1] == 100, f"The last number should be 100, but got {output_numbers[-1]}"



