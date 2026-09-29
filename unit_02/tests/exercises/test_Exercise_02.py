# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to test the area calculation of a rectangle
def run_test(base, height, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_02.py'],  # Path to the script
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{base}\n{height}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Check if the output matches the expected result
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


# Individual test cases

def test_exercise_2_1():
    base = "5.4"
    height = "6.2"
    expected_output = "The area of the rectangle with base = 5.4 and height = 6.2 is 33.48."
    run_test(base, height, expected_output)

def test_exercise_2_2():
    base = "3"
    height = "4"
    expected_output = "The area of the rectangle with base = 3.0 and height = 4.0 is 12.0."
    run_test(base, height, expected_output)

def test_exercise_2_3():
    base = "10"
    height = "20"
    expected_output = "The area of the rectangle with base = 10.0 and height = 20.0 is 200.0."
    run_test(base, height, expected_output)

def test_exercise_2_4():
    base = "7.5"
    height = "3.3"
    expected_output = "The area of the rectangle with base = 7.5 and height = 3.3 is 24.75."
    run_test(base, height, expected_output)
