# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

def test_lesson_2():
    # Run the student's script and capture its output
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_02.py'],
        stdout=subprocess.PIPE,       # Capture stdout
        stderr=subprocess.PIPE,       # Capture stderr
        cwd=UNIT_ROOT,
        text=True                     # Treat input/output as text (strings)
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_02.py should not produce any errors"

    # Expected output from the script
    expected_output = (
        "Statements instruct Python to do something\n"
        "Expressions combine objects and operators and evaluate to an object\n"
        "Statements can include expressions"
    )

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, "The output of Lesson_02.py did not match the expected result"
