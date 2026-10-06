import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Importing from utils


def test_temperature_conversion_celsius_to_fahrenheit():
    """Tests conversion from Celsius to Fahrenheit for a valid positive value."""
    input_sequence = ["1", "20.2"]
    expected_output = "20.2 Celsius is equivalent to 68.36 Fahrenheit"
    
    stdout, stderr = run_program("Exercise_03.py", input_sequence, directory="exercises")

    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output."

    match = re.search(r'([-\d.]+)\s*Celsius is equivalent to\s*([-\d.]+)\s*Fahrenheit', stdout)
    assert match, f"Expected output format not found in: {stdout}"

    input_temp, output_temp = map(float, match.groups())
    assert abs(output_temp - ((9 / 5) * input_temp + 32)) < 0.01, "Incorrect Celsius to Fahrenheit conversion"


def test_temperature_conversion_negative_celsius():
    """Tests that an error is raised for negative Celsius input."""
    input_sequence = ["1", "-2"]
    expected_error_message = "ERROR: You must enter a value of 0 or greater"
    
    stdout, stderr = run_program("Exercise_03.py", input_sequence, directory="exercises")

    assert not stderr, f"Error occurred: {stderr}"
    assert expected_error_message in stdout, f"Expected error message '{expected_error_message}' not found in output."


def test_temperature_conversion_fahrenheit_to_celsius():
    """Tests conversion from Fahrenheit to Celsius for a valid positive value."""
    input_sequence = ["2", "70.25"]
    expected_output = "70.25 Fahrenheit is equivalent to 21.25 Celsius"
    
    stdout, stderr = run_program("Exercise_03.py", input_sequence, directory="exercises")

    assert not stderr, f"Error occurred: {stderr}"
    assert expected_output in stdout, f"Expected '{expected_output}' not found in output."

    match = re.search(r'([-\d.]+)\s*Fahrenheit is equivalent to\s*([-\d.]+)\s*Celsius', stdout)
    assert match, f"Expected output format not found in: {stdout}"

    input_temp, output_temp = map(float, match.groups())
    assert abs(output_temp - ((5 / 9) * (input_temp - 32))) < 0.01, "Incorrect Fahrenheit to Celsius conversion"


def test_temperature_conversion_negative_fahrenheit():
    """Tests that an error is raised for negative Fahrenheit input."""
    input_sequence = ["2", "-2"]
    expected_error_message = "ERROR: You must enter a value of 0 or greater"
    
    stdout, stderr = run_program("Exercise_03.py", input_sequence, directory="exercises")

    assert not stderr, f"Error occurred: {stderr}"
    assert expected_error_message in stdout, f"Expected error message '{expected_error_message}' not found in output."


def test_invalid_option():
    """Tests that an error is raised for an invalid menu option."""
    input_sequence = ["3"]
    expected_error_message = "ERROR: Invalid option"
    
    stdout, stderr = run_program("Exercise_03.py", input_sequence, directory="exercises")

    assert not stderr, f"Error occurred: {stderr}"
    assert expected_error_message in stdout, f"Expected error message '{expected_error_message}' not found in output."


def test_input_prompts():
    """Tests the correctness of input prompts for Celsius and Fahrenheit conversion."""
    stdout, _ = run_program("Exercise_03.py", ["1", "0"], directory="exercises")
    assert "Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:" in stdout, \
        "Initial input prompt is missing or incorrect"
    assert "Please enter the temperature in Celsius:" in stdout, \
        "Celsius input prompt is missing or incorrect"

    stdout, _ = run_program("Exercise_03.py", ["2", "0"], directory="exercises")
    assert "Please enter the temperature in Fahrenheit:" in stdout, \
        "Fahrenheit input prompt is missing or incorrect"
