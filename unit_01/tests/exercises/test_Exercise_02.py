# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import pytest
import subprocess
import sys

import subprocess
import sys

# Helper function to run the multiplication test logic
def run_test(num1, num2, expected_result):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_02.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{num1}\n{num2}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Check if the output format is correct and the calculation is accurate
    expected_output = f"The result of multiplying {num1} and {num2} is {expected_result}."
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


# Individual test cases calling the helper function
def test_exercise_2_1():
    run_test("4", "5", "20")

def test_exercise_2_2():
    run_test("10", "3", "30")

def test_exercise_2_3():
    run_test("0", "100", "0")

def test_exercise_2_4():
    run_test("-2", "7", "-14")
