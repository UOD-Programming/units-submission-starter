import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_05.tests.utils import run_program

def test_scope_namespace_output():
    """Test to check the output of the Lesson_03.py script related to scope and namespaces."""
    
    # Run the script using run_program from utils
    stdout, stderr = run_program("Lesson_03.py", [], directory="lessons")

    # Ensure that there are no errors (stderr should be empty)
    assert stderr.strip() == "", "Lesson_03.py should not produce any errors"

    # Expected output from the script
    expected_output = (
        "When you define a function, you define a new namespace also called a scope.\n\n"
        "Any variable defined within the function is said to be a local variable and can only be accessed inside the function (the scope of the function).\n\n"
        "Calling a function creates a new stack frame and any variable defined in the function scope exists on this stack frame and is local to this stack frame."
    )

    # Compare the actual stdout with the expected output
    assert stdout.strip() == expected_output, f"Expected:\n{expected_output}\n\nGot:\n{stdout.strip()}"