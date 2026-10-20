import sys
import os
from unittest.mock import patch
import io
import random
import inspect

# Add the path to src/exercises (assuming Exercise_05.py is located there)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the functions from Exercise_05.py
from unit_05.src.exercises.Exercise_05 import get_user_guess, print_feedback


def test_get_user_guess_valid_inputs():
    """Test get_user_guess with valid inputs."""
    x = random.randint(1, 10)

    # Mock valid numeric input
    with patch('builtins.input', return_value=str(x)):
        result = get_user_guess()
        assert result == str(x), f"Expected {x} but got {result}"

    # Mock quitting input
    with patch('builtins.input', return_value="q"):
        result = get_user_guess()
        assert result == "q", f"Expected 'q' but got {result}"


def test_get_user_guess_invalid_inputs():
    """Test get_user_guess with invalid inputs and print output."""
    input_strs = ["11", "S", "-5", "10"]
    expected_output = (
        "Please enter a whole number between 1 and 10 or q to quit\n"
        "Invalid input\n\n"
        "Please enter a whole number between 1 and 10 or q to quit\n"
        "Invalid input\n\n"
        "Please enter a whole number between 1 and 10 or q to quit\n"
        "Invalid input\n\n"
        "Please enter a whole number between 1 and 10 or q to quit\n"
    )

    output = []

    def mock_input_func(*args):
        output.append(args[0])
        return input_strs.pop(0)

    def mock_print_func(*args, end="\n"):
        temp_str = " ".join(map(str, args))
        output.append(f"{temp_str}{end}")

    # Patch input and print
    with patch('builtins.input', side_effect=mock_input_func):
        with patch('builtins.print', side_effect=mock_print_func):
            get_user_guess()

    assert "".join(output) == expected_output, "The output for invalid inputs does not match the expected result"


def test_print_feedback():
    """Test print_feedback function with various cases."""
    assert 'print_feedback' in globals(), "print_feedback function is not defined"

    # Ensure print_feedback has 3 arguments
    argspec = inspect.getfullargspec(print_feedback)
    arguments = argspec.args[:len(argspec.args) - len(argspec.defaults)] if argspec.defaults else argspec.args
    assert len(arguments) == 3, "Function print_feedback does not take in 3 positional arguments"

    # Test case 1: Correct guess with fewer attempts
    with patch('sys.stdout', new=io.StringIO()) as captured_output:
        print_feedback(2, 3, 5)
        assert captured_output.getvalue().strip() == "Well done, you used 2/3 guesses to guess the secret number 5."

    # Test case 2: Correct guess on the last attempt
    with patch('sys.stdout', new=io.StringIO()) as captured_output:
        print_feedback(3, 3, 6)
        assert captured_output.getvalue().strip() == "Well done, you used 3/3 guesses to guess the secret number 6."

    # Test case 3: All guesses used without success
    with patch('sys.stdout', new=io.StringIO()) as captured_output:
        print_feedback(4, 3, 9)
        assert captured_output.getvalue().strip() == "Sorry, better luck next time."

