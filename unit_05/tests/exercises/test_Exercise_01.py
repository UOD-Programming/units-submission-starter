import sys
import os
import pytest
from unittest.mock import patch
from io import StringIO

# Add the path to src/exercises
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the functions from Exercise_01.py
from unit_05.src.exercises.Exercise_01 import calc_retail_price, main

def test_calc_retail_price():
    """Test calc_retail_price with various inputs."""
    assert calc_retail_price(5, 40) == 7.0
    assert round(calc_retail_price(25.3, 75), 3) == 44.275

def run_main(input_values, expected_output):
    """Helper function to run the main function and check output."""
    output = StringIO()

    def mock_input(prompt):
        print(prompt, end='')
        return input_values.pop(0)

    with patch('builtins.input', mock_input), patch('sys.stdout', output):
        main()

    actual_output = output.getvalue()
    assert actual_output == expected_output, f"Expected:\n{expected_output}\nGot:\n{actual_output}"

def test_main_case_1():
    """Test the main function with mock inputs (case 1)."""
    run_main(
        input_values=['10', '36'],
        expected_output=(
            'Please enter a wholesale cost:\n'
            'Please enter a markup percentage:\n'
            f"The retail price is £{13.60:.2f}.\n"
        )
    )

def test_main_case_2():
    """Test the main function with mock inputs (case 2)."""
    run_main(
        input_values=['100', '52.3'],
        expected_output=(
            'Please enter a wholesale cost:\n'
            'Please enter a markup percentage:\n'
            f"The retail price is £{152.30:.2f}.\n"
        )
    )
