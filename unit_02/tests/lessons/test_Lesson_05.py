# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]
import re

# Helper function to run the multiplication calculator test logic
def run_test(num1, num2, expected_result):
    # Run the student's script and capture its output
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_05.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{num1}\n{num2}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Extract the calculated result using regex
    match = re.search(r'is ([\d.]+)$', result)
    assert match, f"Output format is incorrect: {result}"
    calculated_result = match.group(1)

    # Check if the output format is correct
    expected_format = f"The result of multiplying {float(num1)} by {float(num2)} is"
    assert result.startswith(expected_format), f"Expected output to start with '{expected_format}', but got '{result}'"

    # Check if the calculation is accurate (allowing for small floating-point differences)
    assert abs(float(calculated_result) - float(expected_result)) < 1e-9, \
        f"Expected result close to {expected_result}, but got {calculated_result}"

# Individual test functions calling the helper function
def test_lesson_5_1():
    run_test("2.1", "3", "6.3")

def test_lesson_5_2():
    run_test("5.2", "3.4", "17.68")

def test_lesson_5_3():
    run_test("10", "0.5", "5.0")

def test_lesson_5_4():
    run_test("0", "100", "0.0")
