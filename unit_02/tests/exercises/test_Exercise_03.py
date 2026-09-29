# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]
import re

# Helper function to run the test logic
def run_test(child, adult, senior, expected_total):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_03.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True,
        encoding='utf-8'  # Specify UTF-8 encoding
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{child}\n{adult}\n{senior}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output (ignoring the input prompts)
    result = stdout.strip().split('\n')[-1]

    # Use regex to extract the total price
    match = re.search(r'Total Price: .?(\d+)', result)
    assert match, f"Output format is incorrect: {result}"

    actual_total = match.group(1)

    # Check if the total price matches the expected result
    assert actual_total == expected_total, f"Expected total of '{expected_total}', but got '{actual_total}'"

    # Check if the output starts with "Total Price: " (allowing for potential encoding issues with £)
    assert result.startswith("Total Price:"), f"Output does not start with 'Total Price:': {result}"


# Individual test cases

def test_exercise_3_1():
    run_test("3", "4", "2", "71")

def test_exercise_3_2():
    run_test("0", "1", "1", "18")

def test_exercise_3_3():
    run_test("5", "0", "0", "25")

def test_exercise_3_4():
    run_test("2", "2", "2", "46")