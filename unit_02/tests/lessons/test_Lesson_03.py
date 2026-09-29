# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to test Lesson_03.py with different input values for a, b, and c
def run_test(user_input, expected_output_lines):
    # Run the student's script and capture its output
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_03.py'],  # Path to the Lesson_03.py script
        stdin=subprocess.PIPE,        # Provide input via stdin
        stdout=subprocess.PIPE,       # Capture stdout
        stderr=subprocess.PIPE,       # Capture stderr
        cwd=UNIT_ROOT,
        text=True                     # Treat input/output as text (strings)
    )

    # Pass the user input to the process and capture the output and errors
    stdout, stderr = process.communicate(input=user_input)

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_03.py should not produce any errors"

    # Split the stdout output by lines
    output_lines = stdout.strip().split('\n')

    # Print the output for debugging
    print(output_lines)

    # Ensure that the number of output lines matches the expected output
    assert len(output_lines) == len(expected_output_lines), "Unexpected number of output lines"

    # Check each line of the output against the expected values
    for i, expected in enumerate(expected_output_lines):
        assert output_lines[i] == expected, f"Line {i + 1} output incorrect. Expected: {expected}, Got: {output_lines[i]}"


# Original test case (a = 2, b = 3, c = 4)
def test_lesson_3_1():
    user_input = "2\n3\n4\n"  # a = 2, b = 3, c = 4
    expected_output_lines = [
        "Please enter a number: Please enter a number: Please enter a number: <class 'float'>",  # Task 1
        str((2 + 3) * 4),  # Task 2
        str(2 ** (3 + 4)),  # Task 2
        "True",  # Task 3 (a < b)
        "True"   # Task 4 (a < b) == (a <= b)
    ]
    run_test(user_input, expected_output_lines)


# New test case 1 (a = 5, b = 2, c = 3)
def test_lesson_3_2():
    user_input = "5\n2\n3\n"  # a = 5, b = 2, c = 3
    expected_output_lines = [
        "Please enter a number: Please enter a number: Please enter a number: <class 'float'>",  # Task 1
        str((5 + 2) * 3),  # Task 2
        str(5 ** (2 + 3)),  # Task 2
        "False",  # Task 3 (a < b)
        "True"   # Task 4 (a < b) == (a <= b)
    ]
    run_test(user_input, expected_output_lines)


# New test case 2 (a = -1, b = 0, c = 2)
def test_lesson_3_3():
    user_input = "-1\n0\n2\n"  # a = -1, b = 0, c = 2
    expected_output_lines = [
        "Please enter a number: Please enter a number: Please enter a number: <class 'float'>",  # Task 1
        str((-1 + 0) * 2),  # Task 2
        str((-1) ** (0 + 2)),  # Task 2
        "True",  # Task 3 (a < b)
        "True"   # Task 4 (a < b) == (a <= b)
    ]
    run_test(user_input, expected_output_lines)


# New test case 3 (a = 7, b = 7, c = 1)
def test_lesson_3_4():
    user_input = "7\n7\n1\n"  # a = 7, b = 7, c = 1
    expected_output_lines = [
        "Please enter a number: Please enter a number: Please enter a number: <class 'float'>",  # Task 1
        str((7 + 7) * 1),  # Task 2
        str(7 ** (7 + 1)),  # Task 2
        "False",  # Task 3 (a < b)
        "False"   # Task 4 (a < b) == (a <= b)
    ]
    run_test(user_input, expected_output_lines)
