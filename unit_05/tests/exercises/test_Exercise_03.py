import sys
import os
import random
import io
from unittest.mock import patch

# Add the path to src/exercises (assuming exercise_3.py is located there)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the main and num_digits functions from exercise_3.py
from unit_05.src.exercises.Exercise_03 import main, num_digits


def run_with_input(input_value):
    """Helper function to run the main function with mock input."""
    
    assert 'main' in globals(), "main function is not defined"
    
    input_mock = lambda _: input_value
    output = io.StringIO()

    with patch('builtins.input', input_mock):
        with patch('sys.stdout', output):
            main()

    return output.getvalue()


def test_main_multiple_digits():
    """Test the main function with random multi-digit input."""
    x = str(random.randint(10, 100000))
    expected_output = f"{x} has {len(str(x))} digits.\n"
    assert run_with_input(x) == expected_output


def test_main_single_digit():
    """Test the main function with random single-digit input."""
    x = str(random.randint(1, 9))
    expected_output = f"{x} has {len(str(x))} digit.\n"
    assert run_with_input(x) == expected_output


def test_main_invalid_input():
    """Test the main function with invalid (non-numeric) input."""
    x = "test"
    expected_output = "Invalid input.\n"
    assert run_with_input(x) == expected_output


def test_num_digits():
    """Test the num_digits function with various cases."""
    assert num_digits(1) == 1, "Expected 1 digit for number 1"
    assert num_digits(23) == 2, "Expected 2 digits for number 23"
    assert num_digits(24626) == 5, "Expected 5 digits for number 24626"
    assert num_digits(2525) == 4, "Expected 4 digits for number 2525"
    assert num_digits(262627) == 6, "Expected 6 digits for number 262627"
    assert num_digits(10 ** 6) == 7, "Expected 7 digits for number 10^6"

