from unittest.mock import patch
import io
import os
import sys

# Add the path to the "Exercise_04.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))
from unit_06.src.exercises.Exercise_04 import main

def run_test(input_values, expected_output):
    input_mock = iter(input_values)
    output = io.StringIO()

    def mock_input(prompt):
        return next(input_mock)

    with patch('builtins.input', mock_input):
        with patch('sys.stdout', output):
            main()

    actual_output = output.getvalue().strip()
    assert actual_output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{actual_output}"

def test_correct_change():
    input_values = ["100", "42"]
    expected_output = (
        "Number of 50p coins is 1\n"
        "Number of 20p coins is 0\n"
        "Number of 10p coins is 0\n"
        "Number of 5p coins is 1\n"
        "Number of 2p coins is 1\n"
        "Number of 1p coins is 1"
    )
    run_test(input_values, expected_output)

def test_correct_change_different_amounts():
    input_values = ["66", "33"]
    expected_output = (
        "Number of 50p coins is 0\n"
        "Number of 20p coins is 1\n"
        "Number of 10p coins is 1\n"
        "Number of 5p coins is 0\n"
        "Number of 2p coins is 1\n"
        "Number of 1p coins is 1"
    )
    run_test(input_values, expected_output)

def test_item_costs_more():
    input_values = ["75", "80"]
    expected_output = (
        "Item costs more than amount inserted"
    )
    run_test(input_values, expected_output)

def test_invalid_amount_over_100():
    input_values = ["105"]
    expected_output = (
        "Invalid amount"
    )
    run_test(input_values, expected_output)

def test_invalid_amount_negative():
    input_values = ["-10"]
    expected_output = (
        "Invalid amount"
    )
    run_test(input_values, expected_output)

def test_exact_amount():
    input_values = ["50", "50"]
    expected_output = (
        "Number of 50p coins is 0\n"
        "Number of 20p coins is 0\n"
        "Number of 10p coins is 0\n"
        "Number of 5p coins is 0\n"
        "Number of 2p coins is 0\n"
        "Number of 1p coins is 0"
    )
    run_test(input_values, expected_output)
