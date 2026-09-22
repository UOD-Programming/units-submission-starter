# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to run the test logic
def run_test(input_number, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_06.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{input_number}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Remove any leading/trailing whitespace and split into lines
    output_lines = stdout.strip().split('\n')

    # Check if we have at least one line of output
    assert output_lines, "No output was produced"

    # Check the multiplication result (should be in the last line of output)
    result_line = output_lines[-1]
    assert result_line == expected_output, \
        f"Expected '{expected_output}', but got '{result_line}'"

    # Optional: Check if the input prompt is present (but don't fail if it's not)
    if len(output_lines) > 1 and "enter a whole number" in output_lines[0].lower():
        print("Input prompt is present.")
    else:
        print("Note: Input prompt is not present or not in the expected format.")


# Individual test cases calling the helper function
def test_lesson_6_1():
    run_test("3", "3x10 = 30")

def test_lesson_6_2():
    run_test("10", "10x10 = 100")

def test_lesson_6_3():
    run_test("0", "0x10 = 0")

def test_lesson_6_4():
    run_test("-5", "-5x10 = -50")
