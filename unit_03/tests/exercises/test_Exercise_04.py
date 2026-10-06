import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from unit_03.tests.utils import find_exercise_file, run_program  # Import from utils


def assert_in_with_encoding(substring, full_string):
    """Replaces pound sign with possible encodings and checks if substring exists in full string."""
    substring = substring.replace('£', '(?:£|Â£)')
    assert re.search(substring, full_string), f"Expected '{substring}' not found in '{full_string}'"


def test_software_pricing_3_copies():
    """Tests pricing with 3 copies (no discount)."""
    copies = 3
    expected_discount = 0
    expected_total = 297.00

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_software_pricing_7_copies():
    """Tests pricing with 7 copies (10% discount)."""
    copies = 7
    expected_discount = 10
    expected_total = 623.70

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_software_pricing_15_copies():
    """Tests pricing with 15 copies (20% discount)."""
    copies = 15
    expected_discount = 20
    expected_total = 1188.00

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_software_pricing_25_copies():
    """Tests pricing with 25 copies (30% discount)."""
    copies = 25
    expected_discount = 30
    expected_total = 1732.50

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_software_pricing_75_copies():
    """Tests pricing with 75 copies (40% discount)."""
    copies = 75
    expected_discount = 40
    expected_total = 4455.00

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_software_pricing_150_copies():
    """Tests pricing with 150 copies (50% discount)."""
    copies = 150
    expected_discount = 50
    expected_total = 7425.00

    stdout, stderr = run_program("Exercise_04.py", [str(copies)], directory="exercises")
    assert not stderr, f"Error occurred: {stderr}"

    assert_in_with_encoding(f"You have been given a {expected_discount}% discount on the normal price of £99.", stdout)
    assert_in_with_encoding(f"The total cost is £{expected_total:.2f}.", stdout)


def test_input_prompt():
    """Tests that the input prompt is correctly displayed."""
    stdout, _ = run_program("Exercise_04.py", ["1"], directory="exercises")
    assert "Please enter the number of copies of the software you wish to purchase:" in stdout, \
        "Input prompt is missing or incorrect"
