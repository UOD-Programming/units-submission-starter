import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_04.tests.utils import run_program  # Import from utils


def normalize_output(output):
    """Removes all whitespace and converts to lowercase."""
    return ''.join(output.lower().split())


def test_guessing_game_multiple_attempts():
    """Tests the output when the user guesses too low, too high, and finally guesses correctly."""
    inputs = [2, 5, 3]  # Guessing sequence: low, high, then correct

    expected_outputs = [
        "Your guess is too low, please try again.",
        "Your guess is too high, please try again.",
        "Well done the correct answer was 3",
        "You took 3 guesses"
    ]

    stdout, stderr = run_program("Exercise_05.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_guessing_game_exit_first_guess():
    """Tests the output when the user exits the game on the first guess."""
    inputs = [0]  # Exiting the game immediately

    expected_outputs = [
        "Program exited",
        "The correct answer was 3"
    ]

    stdout, stderr = run_program("Exercise_05.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_guessing_game_exit_after_low_guess():
    """Tests the output when the user guesses too low, then exits the game."""
    inputs = [2, 0]  # Guessing too low, then exiting

    expected_outputs = [
        "Your guess is too low, please try again.",
        "Program exited",
        "The correct answer was 3"
    ]

    stdout, stderr = run_program("Exercise_05.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_guessing_game_correct_first_attempt():
    """Tests the output when the user guesses correctly on the first try."""
    inputs = [3]  # Guessing the correct number immediately

    expected_outputs = [
        "Well done the correct answer was 3",
        "You took 1 guess"
    ]

    stdout, stderr = run_program("Exercise_05.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


def test_guessing_game_negative_guess():
    """Tests the output when the user enters a negative guess."""
    inputs = [-5, 3]  # Negative guess followed by correct guess

    expected_outputs = [
        "Your guess is too low, please try again.",
        "Well done the correct answer was 3",
        "You took 2 guesses"
    ]

    stdout, stderr = run_program("Exercise_05.py", inputs, directory="exercises")
    normalized_output = normalize_output(stdout)

    for expected in expected_outputs:
        normalized_expected = normalize_output(expected)
        assert normalized_expected in normalized_output, f"For inputs {inputs}:\nExpected output containing: {expected}\nGot: {stdout.strip()}"


