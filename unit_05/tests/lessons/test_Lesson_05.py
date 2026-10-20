import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_05.tests.utils import run_program

def test_help_output():
    """Test to check if the help output of Lesson_05.py contains the correct docstring."""
    
    # Run the script using run_program from utils
    stdout, stderr = run_program("Lesson_05.py", [], directory="lessons")

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_05.py should not produce any errors"

    # Expected keywords from the function's docstring
    expected_keywords = [
        "Find a y such that y**power = x",
        "Parameters",
        "Returns",
        "epsilon: int or float, default 0.01",
        "float or None"
    ]

    # Ensure all expected keywords are found in the stdout (output)
    for keyword in expected_keywords:
        assert keyword in stdout, f"The output does not contain the expected docstring part: {keyword}"
