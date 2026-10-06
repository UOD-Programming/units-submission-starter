import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Import from utils


def extract_fahrenheit_from_output(output):
    match = re.search(r"equivalent to ([\d.]+) Fahrenheit", output)
    if match:
        return float(match.group(1))
    return None


def test_celsius_to_fahrenheit_20_2():
    input_value = "20.2"
    expected_fahrenheit = 68.36
    tolerance = 0.01
    stdout, stderr = run_program("Exercise_01.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"
    
    assert "Please enter the temperature in Celsius:" in stdout, \
        f"Input prompt is incorrect or missing. Expected 'Please enter the temperature in Celsius:', got: {stdout}"

    assert f"{input_value}" in stdout, \
        f"Input value {input_value} not found in output. Got: {stdout}"

    actual_fahrenheit = extract_fahrenheit_from_output(stdout)
    assert actual_fahrenheit is not None, "Could not extract Fahrenheit value from output."

    assert abs(actual_fahrenheit - expected_fahrenheit) < tolerance, \
        f"Expected Fahrenheit value within {tolerance} of {expected_fahrenheit}, but got {actual_fahrenheit}"


def test_celsius_to_fahrenheit_0():
    input_value = "0"
    expected_fahrenheit = 32.0
    tolerance = 0.01
    stdout, stderr = run_program("Exercise_01.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"
    
    assert "Please enter the temperature in Celsius:" in stdout, \
        f"Input prompt is incorrect or missing. Expected 'Please enter the temperature in Celsius:', got: {stdout}"

    assert f"{input_value}" in stdout, \
        f"Input value {input_value} not found in output. Got: {stdout}"

    actual_fahrenheit = extract_fahrenheit_from_output(stdout)
    assert actual_fahrenheit is not None, "Could not extract Fahrenheit value from output."

    assert abs(actual_fahrenheit - expected_fahrenheit) < tolerance, \
        f"Expected Fahrenheit value within {tolerance} of {expected_fahrenheit}, but got {actual_fahrenheit}"


def test_celsius_to_fahrenheit_negative():
    input_value = "-1"
    stdout, stderr = run_program("Exercise_01.py", [input_value], directory="exercises")

    assert not stderr, f"Error occurred during program execution: {stderr}"

    assert stdout.strip() == "Please enter the temperature in Celsius:", \
        f"For negative input, expected no output except for the input prompt. Got: {stdout}"


def test_input_prompt():
    stdout, _ = run_program("Exercise_01.py", ["0"], directory="exercises")
    assert "Please enter the temperature in Celsius:" in stdout, \
        f"Input prompt is missing or incorrect. Expected 'Please enter the temperature in Celsius:', got: {stdout}"
