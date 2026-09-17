# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys

def test_lesson_3():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_03.py'],  # Path to the L1_Exercise.py script
        stdout=subprocess.PIPE,  # Capture stdout
        stderr=subprocess.PIPE,  # Capture stderr
        text=True  # Get output as a string instead of bytes
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    # Ensure that the script runs without errors
    assert stderr.strip() == "", "L1_Exercise.py should not produce any errors"

    # Expected output from the script
    expected_output = (
        "<class 'int'>\n"
        "<class 'float'>\n"
        "<class 'float'>\n"
        "<class 'bool'>"
    )

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, "The output of L1_Exercise.py did not match the expected output"
