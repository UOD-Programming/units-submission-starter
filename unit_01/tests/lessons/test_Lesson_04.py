# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import pytest
import subprocess
import sys



def test_lesson_4():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_04.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Capture the output and errors from the script
    stdout, stderr = process.communicate()

    assert not stderr, f"Script produced errors: {stderr}"

    output_lines = stdout.split('\n')

    # Check each expected output separately
    hello_world_line = None
    division_result = None

    for line in output_lines:
        if line == "Hello World!":
            hello_world_line = line
        elif line.replace('.', '').isdigit():  # Check if the line is a number
            division_result = float(line)

    # Check for "Hello World!" output (fixed NameError)
    assert hello_world_line == "Hello World!", "Expected 'Hello World!' in the output"

    # Check for the division result (fixed TypeError)
    assert division_result is not None, "Expected a numeric result from division"
    assert abs(division_result - 10.0) < 0.001, f"Expected division result close to 10.0, but got {division_result}"

    # Optionally check for "hello world" (fixed SyntaxError)
    if "hello world" in stdout:
        print("Note: 'hello world' is present in the output (SyntaxError fix)")
    else:
        print("Note: 'hello world' is not present in the output (potential missing SyntaxError fix)")
