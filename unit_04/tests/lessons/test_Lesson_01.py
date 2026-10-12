import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils

def test_even_numbers():
    # Run the script using the run_program function from utils
    stdout, stderr = run_program("Lesson_01.py", [], directory="lessons")

    # Split the output into lines
    output = stdout.strip().split('\n')

    # Convert the output to a list of integers
    try:
        output_numbers = [int(num) for num in output]
    except ValueError:
        pytest.fail("The output contains non-integer values")

    # Check if all numbers are even
    assert all(num % 2 == 0 for num in output_numbers), "Not all numbers in the output are even."

    # Check if the numbers are in ascending order
    assert output_numbers == sorted(output_numbers), "The numbers are not in ascending order."

    # Check if the first number is 2 and the last number is 100
    assert output_numbers[0] == 2, f"The first number should be 2, but got {output_numbers[0]}."
    assert output_numbers[-1] == 100, f"The last number should be 100, but got {output_numbers[-1]}."

    # Check if all even numbers between 2 and 100 are present
    expected_numbers = list(range(2, 101, 2))
    assert output_numbers == expected_numbers, "Not all even numbers between 2 and 100 are present."

    # Check the total count of numbers
    assert len(output_numbers) == 50, f"Expected 50 even numbers, but got {len(output_numbers)}."
