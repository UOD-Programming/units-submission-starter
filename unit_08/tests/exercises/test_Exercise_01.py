import pytest
from unittest.mock import patch
from io import StringIO
import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_08.src.exercises.Exercise_01 import validate_input, get_input, check_word, start_game


def test_validate_input():
    assert validate_input("think") is True
    assert validate_input("thinking") is False
    assert validate_input("12345") is False
    assert validate_input("Help&") is False


def test_get_input():
    with patch('builtins.input', side_effect=['test', '12345', 'Help&', 'earnt']):
        assert get_input() == "earnt"


def test_check_word():
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        assert not check_word("error", "tests")
        assert fake_out.getvalue().strip() == "*Y***"

    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        assert not check_word("error", "steer")
        assert fake_out.getvalue().strip() == "**YYG"

    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        assert check_word("error", "error") is True
        assert fake_out.getvalue().strip() == "GGGGG"


def test_start_game():
    with patch('unit_08.src.exercises.Exercise_01.get_input', side_effect=['wrong', 'guess', 'error']), \
         patch('sys.stdout', new_callable=StringIO) as fake_out:
        start_game("error")
        output = fake_out.getvalue()
        assert "Welcome to Derble!" in output
        assert "Congrats! You took 3 attempts." in output
