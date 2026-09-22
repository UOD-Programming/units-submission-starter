# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

def test_lesson_5():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_05.py'],  # Path to the fixed main.py script
        stdout=subprocess.PIPE,       # Capture stdout
        stderr=subprocess.PIPE,       # Capture stderr
        cwd=UNIT_ROOT,
        text=True                     # Get output as a string instead of bytes
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    # Ensure that the script runs without errors (no IndentationError)
    assert stderr.strip() == "", "Lesson_05.py should not produce any errors after fixing indentation"

    # Expected output from the script
    expected_output = (
        "Indentation matters in Python\n"
        "Hello World!"
    )

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, "The output of main.py did not match the expected output"
