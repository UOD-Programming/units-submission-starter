import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Importing from utils


def extract_fahrenheit_from_output(output):
    match = re.search(r"equivalent to ([\d.]+) Fahrenheit", output)
    if match:
        return float(match.group(1))
    return None


def test_temperature_conversion_20_2():
    input_value = "20.2"
    expected_celsius = 20.2
    expected_fahrenheit = 68.36
    tolerance = 0.01

    stdout, stderr = run_program("Exercise_02.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"

    assert "Please enter the temperature in Celsius:" in stdout, \
        f"Input prompt is missing or incorrect. Got: {stdout}"

    assert f"{expected_celsius}" in stdout, \
        f"Expected input value {expected_celsius} not found in output. Got: {stdout}"

    actual_fahrenheit = extract_fahrenheit_from_output(stdout)
    assert actual_fahrenheit is not None, "Could not extract Fahrenheit value from output."

    assert abs(actual_fahrenheit - expected_fahrenheit) < tolerance, \
        f"Expected Fahrenheit value within {tolerance} of {expected_fahrenheit}, but got {actual_fahrenheit}"


def test_temperature_conversion_0():
    input_value = "0"
    expected_celsius = 0
    expected_fahrenheit = 32.0
    tolerance = 0.01

    stdout, stderr = run_program("Exercise_02.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"

    assert "Please enter the temperature in Celsius:" in stdout, \
        f"Input prompt is missing or incorrect. Got: {stdout}"

    assert f"{expected_celsius}" in stdout, \
        f"Expected input value {expected_celsius} not found in output. Got: {stdout}"

    actual_fahrenheit = extract_fahrenheit_from_output(stdout)
    assert actual_fahrenheit is not None, "Could not extract Fahrenheit value from output."

    assert abs(actual_fahrenheit - expected_fahrenheit) < tolerance, \
        f"Expected Fahrenheit value within {tolerance} of {expected_fahrenheit}, but got {actual_fahrenheit}"


def test_temperature_conversion_negative():
    input_value = "-2"
    expected_error_message = "ERROR: You must enter a value of 0 or greater."

    stdout, stderr = run_program("Exercise_02.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"

    assert expected_error_message in stdout, \
        f"Expected error message '{expected_error_message}' for negative input not found. Got: {stdout}"


def test_input_prompt():
    stdout, _ = run_program("Exercise_02.py", ["0"], directory="exercises")
    assert "Please enter the temperature in Celsius:" in stdout, \
        "Input prompt is missing or incorrect."
