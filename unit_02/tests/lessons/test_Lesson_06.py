# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Helper function to run the test logic for Lesson_06.py
def run_test(user_input, expected_output):
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/lessons/Lesson_06.py'],  # Path to the Lesson_06.py script
        stdin=subprocess.PIPE,        # Provide input via stdin
        stdout=subprocess.PIPE,       # Capture stdout
        stderr=subprocess.PIPE,       # Capture stderr
        cwd=UNIT_ROOT,
        text=True                     # Treat input/output as text (strings)
    )

    # Pass the user input to the process and capture the output and errors
    stdout, stderr = process.communicate(input=user_input)

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_06.py should not produce any errors"

    # Check that the stdout matches the expected output
    assert stdout.strip() == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{stdout.strip()}"


# Individual test cases

# Case 1: The quick brown fox jumps over the lazy dog
def test_lesson_6_1():
    user_input = "The quick brown fox jumps over the lazy dog\n"
    expected_output = (
        "Please enter a sentence:\n"
        "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG\n"
        "the quick brown fox jumps over the lazy dog\n"
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    )
    run_test(user_input, expected_output)

# Case 2: Hello world
def test_lesson_6_2():
    user_input = "Hello world\n"
    expected_output = (
        "Please enter a sentence:\n"
        "HELLO WORLD\n"
        "hello world\n"
        "Hello World"
    )
    run_test(user_input, expected_output)

# Case 3: Python is fun
def test_lesson_6_3():
    user_input = "Python is fun\n"
    expected_output = (
        "Please enter a sentence:\n"
        "PYTHON IS FUN\n"
        "python is fun\n"
        "Python Is Fun"
    )
    run_test(user_input, expected_output)

# Case 4: Testing is essential
def test_lesson_6_4():
    user_input = "Testing is essential\n"
    expected_output = (
        "Please enter a sentence:\n"
        "TESTING IS ESSENTIAL\n"
        "testing is essential\n"
        "Testing Is Essential"
    )
    run_test(user_input, expected_output)
