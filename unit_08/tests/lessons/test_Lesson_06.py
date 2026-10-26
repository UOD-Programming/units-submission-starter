from unittest.mock import patch
import pytest
import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_06 import hello, add_three, keyword, funky_func

# Helper function to run tests
def run_test(func, test_values, expected_output, *args, **kwargs):
    input_values = test_values.copy()
    output = []

    def mock_input_func(*args):
        if len(args) > 0:
            output.append(args[0])
        return input_values.pop(0)

    def mock_print_func(*args, end="\n"):
        temp_str = ""
        if len(args) > 0:
            temp_str = " ".join([str(x) for x in args])
        output.append(f"{temp_str}{end}")

    with patch('builtins.input', side_effect=mock_input_func) as mock_input:
        with patch('builtins.print', side_effect=mock_print_func) as mock_print:
            try:
                return_val = func(*args, **kwargs)  # Call unchanged function.
            except Exception as e:
                error = f"Main method failed. {e}"
                output.append(error)

    output = "".join(output)
    expected_output = "".join(expected_output)
    assert output == expected_output, f"Expected:\n{expected_output}\nGot:\n{output}"
    return return_val

# Pytest test cases
def test_hello():
    input_values = []
    expected_output = [
        "Logging function...\nThe functions name is hello\nCalling the function...\nhello\nEnding logging...\n"]
    run_test(hello, input_values, expected_output)


def test_add_three():
    input_values = []
    expected_output = [
        "Logging function...\nThe functions name is add_three\nCalling the function...\n12\nEnding logging...\n"]
    run_test(add_three, input_values, expected_output, 3, 4, 5)


def test_keyword():
    input_values = []
    expected_output = [
        "Logging function...\nThe functions name is keyword\nCalling the function...\n7\nEnding logging...\n"]
    run_test(keyword, input_values, expected_output, a=2)


def test_funky_func():
    input_values = []
    expected_output = [
        "Logging function...\nThe functions name is funky_func\nCalling the function...\n3\n4\n10\nEnding logging...\n"]
    run_test(funky_func, input_values, expected_output, 3, 4, z=10)