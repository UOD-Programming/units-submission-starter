# YOU ARE NOT ALLOWED TO EDIT THIS FILE. 
# EDITING IT WILL CAUSE YOU PROBLEMS
# I WILL ALSO BE NOTIFIED OF THIS WHEN YOU SUBMIT TO GITHUB
import subprocess
import sys
import re


def test_exercise_1():
    # Run the student's script as a subprocess
    process = subprocess.Popen(
        [sys.executable, 'src/exercises/Exercise_01.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Capture the output
    stdout, stderr = process.communicate()

    # Check if there were any errors
    assert not stderr, f"Error occurred: {stderr}"

    # Split the output into lines
    output_lines = stdout.strip().split('\n')

    # Check the expected output
    assert len(output_lines) == 5, "Output should have 5 lines"
    assert output_lines[0] == "Hello and Welcome to Programming in Python."
    assert output_lines[1] == ""
    assert output_lines[
               2] == "Python is a great general purpose language and is used by the likes of Google and Facebook."
    assert output_lines[3] == ""

    # Check if the last line starts with "The current date and time is " and ends with a datetime format
    datetime_pattern = r"The current date and time is \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+"
    assert re.match(datetime_pattern,
                    output_lines[4]), "Last line should contain the current date and time in the correct format"
