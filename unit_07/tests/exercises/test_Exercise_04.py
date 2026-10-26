import os
import sys
from unittest.mock import patch
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the function to be tested
from unit_07.src.exercises.Exercise_04 import count_letters


def run_count_letters_test(func, input_values, expected_output, *args):
    output = []

    def mock_input(*_):
        return input_values.pop(0)

    def mock_print(*args, end="\n"):
        temp_str = " ".join(map(str, args)) + end
        output.append(temp_str)

    with patch('builtins.input', side_effect=mock_input), \
         patch('builtins.print', side_effect=mock_print):
        try:
            func(*args)
        except Exception as e:
            output.append(f"Main method failed. {e}")

    output = "".join(output)
    expected_output = "".join(expected_output)
    assert output == expected_output, f"Expected: {expected_output}, Got: {output}"


def test_letter_count_for_files_case1():
    # Test for test.txt
    expected_output1 = [
        'The count of the letters for the file is:\n\n', 'A: 1\n', 'T: 1\n',
        'W: 1\n', 'a: 3\n', 'c: 1\n', 'd: 3\n', 'e: 5\n', 'f: 2\n', 'g: 1\n',
        'h: 2\n', 'i: 7\n', 'l: 3\n', 'm: 2\n', 'n: 3\n', 'o: 2\n', 'p: 2\n',
        's: 6\n', 't: 1\n', 'w: 1\n'
    ]
    filename = UNIT_ROOT / "src/exercises/Exercise_04_test.txt"
    run_count_letters_test(count_letters, [], expected_output1, filename)


def test_letter_count_for_files_case2():
    # Test for example.txt
    expected_output2 = [
        'The count of the letters for the file is:\n\n', 'A: 2\n', 'C: 4\n', 'D: 5\n', 'E: 1\n', 'F: 2\n',
        'I: 3\n', 'L: 1\n', 'M: 6\n', 'N: 4\n', 'P: 7\n', 'Q: 1\n', 'S: 3\n', 'U: 1\n', 'V: 2\n', 'a: 164\n',
        'b: 26\n', 'c: 87\n', 'd: 52\n', 'e: 251\n', 'f: 20\n', 'g: 40\n', 'h: 7\n', 'i: 171\n', 'j: 1\n',
        'l: 123\n', 'm: 84\n', 'n: 130\n', 'o: 84\n', 'p: 40\n', 'q: 26\n', 'r: 94\n', 's: 144\n', 't: 141\n',
        'u: 153\n', 'v: 25\n', 'x: 5\n'
    ]
    filename = UNIT_ROOT / "src/exercises/Exercise_04_words.txt"
    run_count_letters_test(count_letters, [], expected_output2, filename)
