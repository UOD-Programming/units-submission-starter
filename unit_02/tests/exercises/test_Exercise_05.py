# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to run the test logic for the paint calculator
def run_test(length, height, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_05.py'],  # Path to the Exercise_05.py script
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{length}\n{height}\n")

    # Ensure that there are no errors
    assert stderr.strip() == "", "Exercise_05.py should not produce any errors"

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{stdout.strip()}"


# Individual test cases

# Case 1: Length = 10, Height = 3
def test_exercise_5_1():
    expected_output = (
        "Please enter the length of the wall:\n"
        "Please enter the height of the wall:\n"
        "You require 2 cans of paint."
    )
    run_test(10, 3, expected_output)

# Case 2: Length = 5, Height = 5
def test_exercise_5_2():
    expected_output = (
        "Please enter the length of the wall:\n"
        "Please enter the height of the wall:\n"
        "You require 2 cans of paint."
    )
    run_test(5, 5, expected_output)

# Case 3: Length = 15, Height = 10
def test_exercise_5_3():
    expected_output = (
        "Please enter the length of the wall:\n"
        "Please enter the height of the wall:\n"
        "You require 8 cans of paint."
    )
    run_test(15, 10, expected_output)

# Case 4: Length = 7.5, Height = 3
def test_exercise_5_4():
    expected_output = (
        "Please enter the length of the wall:\n"
        "Please enter the height of the wall:\n"
        "You require 2 cans of paint."
    )
    run_test(7.5, 3, expected_output)
