# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]
import re

# Helper function to run the temperature conversion test logic
def run_test(celsius_input, expected_fahrenheit):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_01.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=celsius_input)

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompt)
    result = stdout.strip().split('\n')[-1]

    # Use regex to extract the Celsius and Fahrenheit values
    match = re.search(r'([-\d.]+)\s*Celsius is equivalent to\s*([-\d.]+)\s*Fahrenheit', result)
    assert match, f"Output format is incorrect: {result}"

    celsius_output, fahrenheit_output = match.groups()

    # Check if the Celsius output is equivalent to the input
    assert float(celsius_output) == float(
        celsius_input), f"Input Celsius {celsius_input} does not match output {celsius_output}"

    # Check if the Fahrenheit output matches the expected value
    assert fahrenheit_output == expected_fahrenheit, f"Expected Fahrenheit {expected_fahrenheit}, but got {fahrenheit_output}"


# Individual test cases calling the helper function
def test_exercise_1_1():
    run_test("20.2", "68.36")

def test_exercise_1_2():
    run_test("0", "32.0")

def test_exercise_1_3():
    run_test("-15", "5.0")

def test_exercise_1_4():
    run_test("100", "212.0")
