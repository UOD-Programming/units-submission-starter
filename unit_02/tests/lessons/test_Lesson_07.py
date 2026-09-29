# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to run the test logic
def run_test(firstname, surname, expected_outputs):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_07.py'],  # Path to the Lesson_07.py script
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )

    # Provide input to the script
    stdout, stderr = process.communicate(input=f"{firstname}\n{surname}\n")

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Split the output into lines
    output_lines = stdout.strip().split('\n')

    # Check the outputs
    for i, expected in enumerate(expected_outputs):
        assert output_lines[i + 2] == expected, f"Expected '{expected}', but got '{output_lines[i + 2]}'"


# Individual test cases calling the helper function

def test_lesson_7_1():
    expected_outputs = [
        "The first character of the first name is J",
        "The last character of the surname is e",
        "The person's initials are J.D",
        "The first 3 characters of the first name are Joh",
        "The last 4 characters of the surname are Doe"
    ]
    run_test("John", "Doe", expected_outputs)


def test_lesson_7_2():
    expected_outputs = [
        "The first character of the first name is A",
        "The last character of the surname is h",
        "The person's initials are A.S",
        "The first 3 characters of the first name are Ali",
        "The last 4 characters of the surname are mith"
    ]
    run_test("Alice", "Smith", expected_outputs)


def test_lesson_7_3():
    expected_outputs = [
        "The first character of the first name is M",
        "The last character of the surname is n",
        "The person's initials are M.J",
        "The first 3 characters of the first name are Mic",
        "The last 4 characters of the surname are rdan"
    ]
    run_test("Michael", "Jordan", expected_outputs)


def test_lesson_7_4():
    expected_outputs = [
        "The first character of the first name is E",
        "The last character of the surname is n",
        "The person's initials are E.W",
        "The first 3 characters of the first name are Emm",
        "The last 4 characters of the surname are tson"
    ]
    run_test("Emma", "Watson", expected_outputs)

