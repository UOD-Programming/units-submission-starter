# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

def test_lesson_1():
    # Run the student's script and capture its output
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_01.py'],  # Ensure the correct Python executable is used
        stdout=subprocess.PIPE,  # Capture stdout
        stderr=subprocess.PIPE,  # Capture stderr
        cwd=UNIT_ROOT,
        text=True                # Treat output as text (not bytes)
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    # Ensure there are no errors
    assert stderr.strip() == "", f"Lesson_01.py produced errors: {stderr}"

    # Strip whitespace from the output
    output = stdout.strip()

    # Expected output
    expected_output = (
        "The circle with radius = 6 has circumference = 37.68\n"
        "The circle with radius = 15 has circumference = 94.2"
    )

    # Assert that the output matches the expected output
    assert output == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{output}"
