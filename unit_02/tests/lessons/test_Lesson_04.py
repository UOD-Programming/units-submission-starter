# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

def test_lesson_4():
    # Run the student's script and capture its output
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_04.py'],  # Path to the Lesson_04.py script
        stdout=subprocess.PIPE,       # Capture stdout
        stderr=subprocess.PIPE,       # Capture stderr
        cwd=UNIT_ROOT,
        text=True                     # Treat input/output as text (strings)
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_04.py should not produce any errors"

    # Expected output from the script
    expected_output = (
        "Programming in Python\n"
        "Programming in Python with single quotes\n"
        "I know how to put \"quotes\" into a string.\n"
        "\n"
        "And put in new lines!\n"
        "I am using a multiline string to:\n"
        "- print multiple lines\n"
        "- without the use of the escape character \\n\n"
        "Hi, I am string 1 and I am string 2!\n"
        "string 1 is before string 2 and string 2 is after string 1"
    )

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, "The output of Lesson_04.py did not match the expected result"
