# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys

def test_lesson_2():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_02.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Capture the output
    stdout, stderr = process.communicate()

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Remove any leading/trailing whitespace and newlines
    output = stdout.strip()

    # Check if the output is exactly "Hello World!"
    assert output == "Single line comments start with #", f"Expected 'Single line comments start with #', but got '{output}'"
