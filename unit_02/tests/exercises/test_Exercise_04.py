# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to run the test logic for name manipulation
def run_test(firstname, middlename, lastname, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_04.py'],  # Path to the Lesson_07.py script
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{firstname}\n{middlename}\n{lastname}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Get the last line of output
    result = stdout.strip().split('\n')[-1]

    # Check if the output matches the expected result
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


def test_exercise_4_1():
    expected_output = "Hi, your initials are N.R.M"  # Expected output for Nelson Rolihlahla Mandela
    run_test("Nelson", "Rolihlahla", "Mandela", expected_output)


def test_exercise_4_2():
    expected_output = "Hi, your initials are A.M.T"  # Expected output for Alan Mathison Turing
    run_test("Alan", "Mathison", "Turing", expected_output)


def test_exercise_4_3():
    expected_output = "Hi, your initials are R.P.F"  # Expected output for Richard Phillips Feynman
    run_test("Richard", "Phillips", "Feynman", expected_output)


def test_exercise_4_4():
    expected_output = "Hi, your initials are A.A.K"  # Expected output for Augusta Ada King
    run_test("Augusta", "Ada", "King", expected_output)
